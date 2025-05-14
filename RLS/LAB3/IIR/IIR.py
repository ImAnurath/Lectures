import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sampling frequency
fs = 1000  # 1 kHz (from your ADC code)
# Cutoff frequency (0.25 * fs = 250 Hz)
fc = 0.25 * fs
# Normalized cutoff frequency (required by scipy)
wc = fc / (fs/2)  # = 0.5

# Design an 8th order Butterworth IIR low-pass filter
order = 8
sos = signal.butter(order, wc, btype='low', output='sos')

# Convert to second-order sections to b, a coefficients for each section
num_sections = sos.shape[0]
print("IIR Filter Coefficients (Second-Order Sections):")
print("const float iir_sos[{}][6] = {{".format(num_sections))
for i in range(num_sections):
    print("    {", end="")
    for j in range(5):
        print("{:.10f}f, ".format(sos[i, j]), end="")
    print("{:.10f}f".format(sos[i, 5]), end="")
    if i < num_sections - 1:
        print("},")
    else:
        print("}")
print("};")

# Compute frequency response
w, h = signal.sosfreqz(sos, worN=8000, fs=fs)

# Plot the frequency response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(np.maximum(np.abs(h), 1e-10)))
plt.title('IIR Filter Frequency Response')
plt.ylabel('Amplitude [dB]')
plt.axvline(x=fc, color='r', linestyle='--', alpha=0.7, label=f'Cutoff: {fc} Hz')
plt.grid(True)
plt.legend()

# Plot the phase response
plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(h)))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [rad]')
plt.grid(True)
plt.tight_layout()
plt.savefig('iir_filter_response.png')

# Compute and plot impulse response
b, a = sos2tf(sos)
t, imp = signal.impulse((b, a), N=100)

t = t * 1000  # Convert to milliseconds
plt.figure(figsize=(10, 4))
plt.plot(t, imp)
plt.title('IIR Filter Impulse Response')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('iir_impulse_response.png')

# Plot pole-zero diagram
z, p, k = signal.sos2zpk(sos)
plt.figure(figsize=(6, 6))
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='b', facecolors='none', label='Zeros')
plt.scatter(np.real(p), np.imag(p), marker='x', color='r', label='Poles')
plt.title('Pole-Zero Diagram')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.legend()
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.axis('equal')
plt.savefig('iir_pole_zero.png')

# Convert SOS to transfer function for display
b, a = signal.sos2tf(sos)

# Print the transfer function in Z-domain
print("\nIIR Transfer Function (Z-domain):")

# Numerator
print("            ", end="")
for i in range(len(b)):
    if i == 0:
        print("{:.6f}".format(b[i]), end="")
    else:
        print(" + {:.6f}·z^-{}".format(b[i], i), end="")
print("")

# Denominator
print("H(z) = ---------------------------------")
print("            ", end="")
for i in range(len(a)):
    if i == 0:
        print("{:.6f}".format(a[i]), end="")
    else:
        print(" + {:.6f}·z^-{}".format(a[i], i), end="")
print("\n")

# Print the filter order and cutoff frequency
print(f"Filter Order: {order}")
print(f"Cutoff Frequency: {fc} Hz (normalized: {wc:.2f}π rad/sample)")
print(f"Number of Second-Order Sections: {num_sections}")