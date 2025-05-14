import numpy as np
import matplotlib.pyplot as plt

# Replace with path to your CSV
data = np.loadtxt("sdm_output.csv", delimiter=",")
fs = 1000000  # Sampling frequency (Hz)

# Plot waveform
plt.figure()
plt.plot(data)
plt.title("Signal Waveform")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

# FFT
spectrum = np.fft.fft(data)
freqs = np.fft.fftfreq(len(data), 1/fs)

plt.figure()
plt.plot(freqs[:len(freqs)//2], np.abs(spectrum[:len(spectrum)//2]))
plt.title("Signal Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
