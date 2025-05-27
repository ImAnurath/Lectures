import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
alpha = 1           # Exponential damping constant in s^-1
w_0 = 1             # Angular frequency in rad/s
Fd = 100            # Sampling frequency in Hz
T = 1 / Fd          # Sampling period
t_max = 6.28        # Maximum time for signal calculation in seconds
N = int(t_max * Fd) # Number of time samples

# Time vector from 0 to t_max
t = np.linspace(0, t_max, N)

# Define the time-domain signal s(t) = e^(-alpha * t) * cos(w_0 * t) * u(t)
s_t = np.exp(-alpha * t) * np.cos(w_0 * t)


plt.figure(figsize=(10, 5))
plt.plot(t, s_t, label=r'$s(t) = e^{-\alpha t} \cos(\w_0 t)$')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Time-Domain Signal $s(t)$')
plt.legend()
plt.grid(True)
plt.show()

# Complex frequency parameters
sigma_min, sigma_max = -2, 0           # Range of sigma
w_min, w_max = -2 * w_0, 2 * w_0       # Range of omega
sigma_points = 100
omega_points = 100

# Generate meshgrid for complex frequency plane
sigma = np.linspace(sigma_min, sigma_max, sigma_points)
omega = np.linspace(w_min, w_max, omega_points)
sigma_grid, omega_grid = np.meshgrid(sigma, omega)

# Compute the complex frequency s = sigma + j*omega
s_complex = sigma_grid + 1j * omega_grid

# Compute the complex frequency response S(s) = 1 / (s + alpha - j*w_0)
S_s = 1 / (s_complex + alpha - 1j * w_0)

# Plot the 3D surface of |S(s)| in the complex frequency plane
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(sigma_grid, omega_grid, np.abs(S_s), cmap='viridis')
ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$\omega$')
ax.set_zlabel(r'$|S(s)|$')
ax.set_title('Complex Frequency Response $|S(s)|$')
plt.show()

# Cross-sectional 2D plot of |S(s)| at a fixed sigma just to the right of the pole
sigma_fixed = -0.9  # Just to the right of the pole at -1
s_fixed = sigma_fixed + 1j * omega
S_fixed = 1 / (s_fixed + alpha - 1j * w_0)

# Plot the 2D cross-section |S(sigma + j*omega)|
plt.figure(figsize=(10, 5))
plt.plot(omega, np.abs(S_fixed), label=r'$|S(s)|$ at $\sigma = -0.9$')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|S(s)|$')
plt.title('Cross-Section of $|S(s)|$ at $\sigma = -0.9$')
plt.legend()
plt.grid(True)
plt.show()
