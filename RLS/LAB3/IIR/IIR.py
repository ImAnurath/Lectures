import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sampling frequency and cutoff
fs = 1000  # Hz
fc = 250   # Hz
wc = fc / (fs / 2)  # Normalized cutoff: 0.5 (same as FIR)

# Filter order (2nd-order sections → 4th order total)
order = 16

# Design Butterworth IIR low-pass filter
b, a = signal.butter(order, wc, btype='low', analog=False)

# Print coefficients for ESP32 (in C-style array)
print("IIR Filter Coefficients (b - numerator):")
print("const float iir_b[] = {")
for i, coef in enumerate(b):
    comma = ',' if i < len(b)-1 else ''
    print(f"    {coef:.10f}f{comma}")
print("};")

print("IIR Filter Coefficients (a - denominator):")
print("const float iir_a[] = {")
for i, coef in enumerate(a):
    comma = ',' if i < len(a)-1 else ''
    print(f"    {coef:.10f}f{comma}")
print("};")

# Frequency response
w, h = signal.freqz(b, a)
freq = w * fs / (2 * np.pi)

# Amplitude response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(freq, 20 * np.log10(abs(h)))
plt.title('IIR Filter Frequency Response (Butterworth)')
plt.ylabel('Amplitude [dB]')
plt.axvline(x=fc, color='r', linestyle='--', alpha=0.7, label=f'Cutoff: {fc} Hz')
plt.grid(True)
plt.legend()

# Phase response
plt.subplot(2, 1, 2)
plt.plot(freq, np.unwrap(np.angle(h)))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [rad]')
plt.grid(True)
plt.tight_layout()
plt.savefig('iir_filter_response.png')

# Impulse response
impulse = np.zeros(50)
impulse[0] = 1
response = signal.lfilter(b, a, impulse)
plt.figure(figsize=(10, 4))
plt.stem(response, basefmt=" ")
plt.title('IIR Filter Impulse Response')
plt.xlabel('n [samples]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('iir_impulse_response.png')

# Pole-zero plot
z, p, k = signal.tf2zpk(b, a)
plt.figure(figsize=(6, 6))
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='b', facecolors='none', label='Zeros')
plt.scatter(np.real(p), np.imag(p), marker='x', color='r', label='Poles')
plt.title('IIR Filter Pole-Zero Diagram')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.legend()
plt.axhline(0, color='k', linestyle='--', alpha=0.3)
plt.axvline(0, color='k', linestyle='--', alpha=0.3)
plt.axis('equal')
plt.savefig('iir_pole_zero.png')

# Transfer function (Z-domain)
print("\nIIR Transfer Function (Z-domain):")
print("Numerator H(z): ", end="")
for i, coef in enumerate(b):
    if i == 0:
        print(f"{coef:.6f}", end="")
    else:
        print(f" + {coef:.6f}·z^-{i}", end="")
print()

print("Denominator H(z): ", end="")
for i, coef in enumerate(a):
    if i == 0:
        print(f"{coef:.6f}", end="")
    else:
        print(f" + {coef:.6f}·z^-{i}", end="")
print()

# Summary
print(f"\nIIR Filter Order: {order}")
print(f"Cutoff Frequency: {fc} Hz (normalized: {wc:.2f}π rad/sample)")
