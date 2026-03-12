import numpy as np
import matplotlib.pyplot as plt
import serial

# Configure serial port
ser = serial.Serial('COM4', 115200, timeout=2)  # Change COM port if needed

timestamps = []
voltages = []

print("Collecting data...")
try:
    while len(timestamps) < 1000:
        line = ser.readline().decode().strip()
        if ',' in line:
            try:
                t, v = map(int, line.split(','))
                timestamps.append(t)
                voltages.append(v)
            except ValueError:
                continue
finally:
    ser.close()

timestamps = np.array(timestamps)
voltages = np.array(voltages) / 1000.0

# Plot time-domain signal
plt.figure(figsize=(10, 4))
plt.plot(timestamps - timestamps[0], voltages)
plt.title("ADC Sampled Signal (Time Domain)")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.grid(True)

# Plot FFT
fs = 1000  # Sampling frequency in Hz
n = len(voltages)
fft_vals = np.fft.fft(voltages)
freqs = np.fft.fftfreq(n, d=1/fs)

plt.figure(figsize=(10, 4))
plt.plot(freqs[1:n//2], np.abs(fft_vals[1:n//2])) # First value peeks from the previous reading so we remove it for to visualize the clean reading.
plt.title("FFT Amplitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()
plt.show()