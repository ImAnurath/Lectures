import serial
import numpy as np
import matplotlib.pyplot as plt

# === Configuration ===
COM_PORT = 'COM4'
BAUD_RATE = 115200
NUM_SAMPLES = 1024
SAMPLE_INTERVAL_US = 1000  # in microseconds (1 ms)
SAMPLE_RATE_HZ = 1_000_000 / SAMPLE_INTERVAL_US  # 1000 Hz

# === Read Serial Data ===
ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=2)
print(f"Reading {NUM_SAMPLES} samples from {COM_PORT}...")

samples = []

while len(samples) < NUM_SAMPLES:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            samples.append(float(line))
    except ValueError:
        continue  # Skip invalid lines

ser.close()
print("Data capture complete.")

# === Convert to NumPy Array ===
data = np.array(samples)

# === Time Axis ===
time = np.arange(NUM_SAMPLES) * (SAMPLE_INTERVAL_US / 1e6)  # seconds

# === FFT Analysis ===
fft_vals = np.fft.fft(data)
fft_freq = np.fft.fftfreq(NUM_SAMPLES, d=1/SAMPLE_RATE_HZ)
magnitude = np.abs(fft_vals)[:NUM_SAMPLES // 2]
frequencies = fft_freq[:NUM_SAMPLES // 2]

# === Plotting ===
plt.figure(figsize=(12, 5))

# --- Time Domain (Waveform) ---
plt.subplot(1, 2, 1)
plt.plot(time/2, data/2)
plt.title("Time Domain (Waveform)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# --- Frequency Domain (Magnitude Spectrum) ---
plt.subplot(1, 2, 2)
plt.plot(frequencies, magnitude)
plt.title("Frequency Domain (Spectrum)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()
