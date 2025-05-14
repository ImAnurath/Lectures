import serial
import numpy as np
import matplotlib.pyplot as plt

# === Configuration ===
PORT = 'COM4'
BAUD = 115200
SAMPLES = 500     # Number of ADC samples to collect
SAMPLING_RATE = 100  # Hz

# === Serial Setup ===
ser = serial.Serial(PORT, BAUD, timeout=1)
adc_values = []

print("Reading serial data...")

# === Read SAMPLES values ===
while len(adc_values) < SAMPLES:
    try:
        line = ser.readline().decode().strip()
        if line.isdigit():
            adc_values.append(int(line))
    except:
        continue

ser.close()

# === Convert ADC to Voltage ===
voltages = np.array(adc_values) * 3 / 4095  # 12-bit ADC
time = np.arange(len(voltages)) / SAMPLING_RATE

# === Apply FFT ===
fft_result = np.fft.fft(voltages)  # FFT of the signal
fft_freq = np.fft.fftfreq(SAMPLES, d=1/SAMPLING_RATE)  # Frequency bins
fft_amplitude = np.abs(fft_result)  # Amplitude spectrum
fft_phase = np.angle(fft_result)    # Phase spectrum

# === Plot Time Domain Signal ===
plt.figure(figsize=(10, 4))
plt.plot(time, voltages, label="Signal")
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("ADC Signal (Time Domain)")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Plot Amplitude Spectrum ===
plt.figure(figsize=(10, 4))
plt.plot(fft_freq[:SAMPLES//2], fft_amplitude[:SAMPLES//2])
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.title("Amplitude Spectrum")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Plot Phase Spectrum ===
plt.figure(figsize=(10, 4))
plt.plot(fft_freq[:SAMPLES//2], fft_phase[:SAMPLES//2])
plt.xlabel("Frequency [Hz]")
plt.ylabel("Phase [radians]")
plt.title("Phase Spectrum")
plt.grid(True)
plt.tight_layout()
plt.show()
