# Task1
import numpy as np
import matplotlib.pyplot as plt

N = 4
n = np.arange(N)
x = np.piecewise(n, [n >= 0, (n >= 0) & (n <= 2)], [1, 1]) # This just gives 1 now so it is more like the new n?
dft = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        dft[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
magnitude = np.abs(dft)
angle = np.angle(dft)
print(angle)
plt.figure(figsize=(12, 6))

# Plot the original signal x(n)
plt.subplot(1, 3, 1)
plt.stem(np.arange(N), x)
plt.title('Original Signal x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.xticks(np.arange(N))
plt.grid()

# Plot the magnitude |X[k]|
plt.subplot(1, 3, 2)
plt.stem(np.arange(N), magnitude)
plt.title('Magnitude |X[k]|')
plt.xlabel('k')
plt.ylabel('|X[k]|')
plt.xticks(np.arange(N))
plt.grid()

# Plot the phase angle of X[k]
plt.subplot(1, 3, 3)
plt.stem(np.arange(N), angle)
plt.title('Phase Angle of X[k]')
plt.xlabel('k')
plt.ylabel('Angle (radians)')
plt.xticks(np.arange(N))
plt.grid()
plt.tight_layout(pad= 2.0)
plt.show()
#AV