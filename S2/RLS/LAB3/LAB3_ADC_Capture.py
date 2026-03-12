import serial
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq

# ====== Configuration ======
SERIAL_PORT = 'COM4'        # Change to your ESP32 port (e.g., 'COM3', '/dev/ttyUSB0')
BAUD_RATE = 115200          # Must match your Arduino sketch
CSV_FILENAME = 'adc_data.csv'
SAMPLE_RATE = 1000          # Hz (based on your 1000 microsecond interval)
NUM_SAMPLES = 1024           # /2 is to visualize better

def capture_data():
    """Capture data from the ESP32 and save to CSV"""
    print(f"Opening serial port {SERIAL_PORT} at {BAUD_RATE} baud...")
    
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=10)
        time.sleep(2)  # Allow time for serial connection to establish
        
        # Clear any buffered data
        ser.reset_input_buffer()
        
        # Create and open CSV file
        with open(CSV_FILENAME, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Index', 'Value'])  # Write header
            
            print(f"Waiting for data from ESP32...")
            
            # Read initial message from ESP32
            line = ser.readline().decode('utf-8').strip()
            print(f"ESP32: {line}")
            
            # Read and store samples
            samples_received = 0
            start_time = time.time()
            
            while samples_received < NUM_SAMPLES:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    
                    try:
                        # Split by comma
                        parts = line.split(',')
                        if len(parts) == 2:
                            index = int(parts[0])
                            value = int(parts[1])
                            
                            # Write to CSV
                            csv_writer.writerow([index, value])
                            samples_received += 1
                            
                            # Show progress
                            if samples_received % 100 == 0:
                                print(f"Received {samples_received}/{NUM_SAMPLES} samples...")
                    except ValueError:
                        print(f"Skipping invalid line: {line}")
                
                # Check for timeout (10 seconds)
                if time.time() - start_time > 10:
                    print("Timeout waiting for data. Check your connections.")
                    break
            
            print(f"Data collection complete. Saved {samples_received} samples to {CSV_FILENAME}")
        
        ser.close()
        return samples_received == NUM_SAMPLES
    
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return False

def analyze_data():
    """Analyze the captured data and display plots"""
    print(f"Analyzing data from {CSV_FILENAME}...")
    
    # Read data from CSV
    indices = []
    values = []
    
    with open(CSV_FILENAME, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header
        
        for row in csv_reader:
            indices.append(int(row[0]))
            values.append(int(row[1]))
    
    # Convert to numpy arrays for analysis
    indices = np.array(indices)
    values = np.array(values)
    
    # Create time array in milliseconds
    time_ms = indices * (1000 / SAMPLE_RATE)
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: Time domain waveform
    ax1.plot(time_ms, values, 'b-')
    ax1.set_title('ADC Signal Waveform')
    ax1.set_xlabel('Time (ms)')
    ax1.set_ylabel('ADC Value (12-bit)')
    ax1.grid(True)
    
    # Calculate FFT 
    fft_values = fft(values)
    # Only take first half (due to symmetry of real signal FFT)
    n = len(values)
    freq = fftfreq(n, 1/SAMPLE_RATE)[:n//2]
    fft_magnitude = 2.0/n * np.abs(fft_values[0:n//2])
    
    # Plot 2: Frequency domain spectrum
    ax2.plot(freq, fft_magnitude, 'r-')
    ax2.set_title('Frequency Spectrum')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Magnitude')
    ax2.grid(True)
    ax2.set_xlim(0, SAMPLE_RATE/2)  # Only show up to Nyquist frequency
    
    # Display max values
    max_adc = np.max(values)
    min_adc = np.min(values)
    peak_freq_idx = np.argmax(fft_magnitude[1:]) + 1  # Skip DC component
    peak_freq = freq[peak_freq_idx]
    
    print(f"Signal Analysis Results:")
    print(f"- Peak-to-peak ADC value: {max_adc - min_adc}")
    print(f"- Max ADC value: {max_adc}")
    print(f"- Min ADC value: {min_adc}")
    print(f"- Mean ADC value: {np.mean(values):.2f}")
    print(f"- Dominant frequency: {peak_freq:.2f} Hz")
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function"""
    print("ESP32 ADC Signal Capture and Analysis")
    print("====================================")
    
    # Ask if user wants to capture new data or analyze existing
    choice = input("Do you want to capture new data from ESP32? (y/n): ").lower()
    
    if choice == 'y':
        success = capture_data()
        if success:
            analyze_data()
        else:
            print("Data capture failed. Cannot proceed with analysis.")
    else:
        analyze_data()

if __name__ == "__main__":
    main()