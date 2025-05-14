import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sampling frequency
fs = 1000  # 1 kHz (from your ADC code)
# Cutoff frequency (0.25 * fs = 250 Hz)
fc = 0.25 * fs
# Normalized cutoff frequency (required by scipy)
wc = fc / (fs/2)  # = 0.5

# Design a 16th order FIR low-pass filter (17 coefficients)
numtaps = 17  # 16th order filter has 17 coefficients
fir_coeff = signal.firwin(numtaps, wc, window='hamming')

# Print coefficients for later use in ESP32
print("FIR Filter Coefficients:")
print("const float fir_coeffs[] = {")
for i, coef in enumerate(fir_coeff):
    if i < numtaps - 1:
        print(f"    {coef:.10f}f,")
    else:
        print(f"    {coef:.10f}f")
print("};")

# Compute frequency response
w, h = signal.freqz(fir_coeff)
freq = w * fs / (2 * np.pi)

# Plot the frequency response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(freq, 20 * np.log10(abs(h)))
plt.title('FIR Filter Frequency Response')
plt.ylabel('Amplitude [dB]')
plt.axvline(x=fc, color='r', linestyle='--', alpha=0.7, label=f'Cutoff: {fc} Hz')
plt.grid(True)
plt.legend()

# Plot the phase response
plt.subplot(2, 1, 2)
plt.plot(freq, np.unwrap(np.angle(h)))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [rad]')
plt.grid(True)
plt.tight_layout()
plt.savefig('fir_filter_response.png')

# Plot impulse response
plt.figure(figsize=(10, 4))
plt.stem(np.arange(numtaps), fir_coeff)
plt.title('FIR Filter Impulse Response')
plt.xlabel('n [samples]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('fir_impulse_response.png')

# Plot pole-zero diagram
plt.figure(figsize=(6, 6))
z, p, k = signal.tf2zpk(fir_coeff, [1.0])
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
plt.savefig('fir_pole_zero.png')

# Print the transfer function in Z-domain
print("\nFIR Transfer Function (Z-domain):")
print("H(z) = ", end="")
for i, coef in enumerate(fir_coeff):
    if i == 0:
        print(f"{coef:.6f}", end="")
    else:
        print(f" + {coef:.6f}·z^-{i}", end="")
print("\n")

# Print the filter order and cutoff frequency
print(f"Filter Order: {numtaps-1}")
print(f"Cutoff Frequency: {fc} Hz (normalized: {wc:.2f}π rad/sample)")