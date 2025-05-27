#Task1
import numpy as np
import matplotlib.pyplot as plt

f0 = 10e3  # 10000
w0 = 2 * np.pi * f0  # Angular frequency (rad/s)

t = np.linspace(-0.5e-3, 0.5e-3,1000) # Time range from -0.5 ms to 0.5 ms, 1000 samples

# Sinc function: s(t) = sin(w0 * t) / (w0 * t)
s_t = np.sinc(w0 * t / np.pi)

plt.plot(t * 1e3, s_t)  # Time to ms for better visualization
plt.title("Sinc Function for $f_0 = 10 \, \mathrm{kHz}$")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
#AV