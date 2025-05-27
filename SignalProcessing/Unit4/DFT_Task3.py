# Task1
import numpy as np
import matplotlib.pyplot as plt

N = 4
n = np.arange(N)
first = np.piecewise(n, [n >= 0, (n >= 0) & (n <= 2)], [0, 1])
second = np.piecewise(n, [n >= 0, (n >= 0) & (n <= 2)], [1, 1])

dft_first = np.zeros(N, dtype=complex)
dft_second = np.zeros(N, dtype=complex)

for k in range(N):
    for n in range(N):
        dft_first[k] += first[n] * np.exp(-2j * np.pi * k * n / N)
        dft_second[k] += second[n] * np.exp(-2j * np.pi * k * n / N)
magnitude_first = np.abs(dft_first)
angle_first = np.angle(dft_first)
magnitude_second = np.abs(dft_second)
angle_second = np.angle(dft_second)

reverse_first = np.zeros(N, dtype=complex)
reverse_second = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        reverse_first[k]  += dft_first[n] * np.exp(2j * np.pi * k * n / N)
        reverse_second[k] += dft_second[n] * np.exp(2j * np.pi * k * n / N)

plt.figure(figsize=(12, 6))
plt.suptitle("First DFT Signal [1, 1, 1, 0]", fontsize=16)

plt.subplot(1, 3, 1)
plt.stem(np.arange(N), first)
plt.title('Original Signal x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.xticks(np.arange(N))
plt.grid()

# Plot the magnitude |X[k]|
plt.subplot(1, 3, 2)
plt.stem(np.arange(N), magnitude_first)
plt.title('Magnitude |X[k]|')
plt.xlabel('k')
plt.ylabel('|X[k]|')
plt.xticks(np.arange(N))
plt.grid()

# Plot the phase angle of X[k]
plt.subplot(1, 3, 3)
plt.stem(np.arange(N), angle_first)
plt.title('Phase Angle of X[k]')
plt.xlabel('k')
plt.ylabel('Angle (radians)')
plt.xticks(np.arange(N))
plt.grid()

plt.figure(figsize=(12, 6))
plt.suptitle("Second DFT Signal [1, 1, 1, 1]", fontsize=16)

plt.subplot(1, 3, 1)
plt.stem(np.arange(N), second)
plt.title('Original Signal x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.xticks(np.arange(N))
plt.grid()

# Plot the magnitude |X[k]|
plt.subplot(1, 3, 2)
plt.stem(np.arange(N), magnitude_second)
plt.title('Magnitude |X[k]|')
plt.xlabel('k')
plt.ylabel('|X[k]|')
plt.xticks(np.arange(N))
plt.grid()

# Plot the phase angle of X[k]
plt.subplot(1, 3, 3)
plt.stem(np.arange(N), angle_second)
plt.title('Phase Angle of X[k]')
plt.xlabel('k')
plt.ylabel('Angle (radians)')
plt.xticks(np.arange(N))
plt.grid()

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(np.arange(N), reverse_first.real, label='Real Part', color='b')
plt.plot(np.arange(N), reverse_first.imag, label='Imaginary Part', color='r', linestyle='--')
plt.title('Inverse DFT of dft_first')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.legend()

# Plotting reverse_second
plt.subplot(2, 1, 2)
plt.plot(np.arange(N), reverse_second.real, label='Real Part', color='b')
plt.plot(np.arange(N), reverse_second.imag, label='Imaginary Part', color='r', linestyle='--')
plt.title('Inverse DFT of dft_second')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.legend()

plt.show()
#AV