#Task1
import numpy as np
import matplotlib.pyplot as plt

period = 0.0002 
t = np.linspace(0, period, 1000) 
amp = 1 / (2 * np.pi)
f1 = 4000
f2  = 1000
original_signal = amp * np.cos(2 * np.pi * f1 * t) * np.cos(2 * np.pi * f2 * t)

A_1 = 1/ 4*np.pi
A_2 = 1/ 4*np.pi
w1 = 5000*np.pi
w2 = 3000*np.pi
new_signal = A_1 * np.cos(w1*t) + A_2 * np.cos(w2*t)

fft_new_signal = np.fft.fft(new_signal)
n = len(new_signal)
freq = np.fft.fftfreq(n, period / n)

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, original_signal, label="Original Signal", color='b')
plt.title("Original Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, new_signal, label="Expanded Signal", color='r')
plt.title("Expanded Signal using cos(x)cos(y) identity")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(freq[:n // 2], np.abs(fft_new_signal)[:n // 2], label="Expanded Signal", color='r') # Slicing negative frequencies
plt.title("Frequency Domain")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()
plt.show()
#AV