#Task3
import numpy as np
import matplotlib.pyplot as plt
# Define time range
t = np.linspace(-10, 10, 1000)
T = 1
# Define rectangular pulse: 1 between -0.5 and 0.5, 0 elsewhere
# Define pulse width


# X(t - T/2)
rect_pulse_1 = np.piecewise(t, [np.abs(t - T/2) <= T/2, np.abs(t - T/2) > T/2], [1, 0])
# X(t - 3T/2)
rect_pulse_2 = np.piecewise(t, [np.abs(t - 3*T/2) <= T/2, np.abs(t - 3*T/2) > T/2], [1, 0])
# X(t/2 - T/2)
rect_pulse_3 = np.piecewise(t, [np.abs(t/2 - T/2) <= T/2, np.abs(t/2 - T/2) > T/2], [1, 0])

'''FFT and Phase of rectangular pulses'''
# X(t - T/2)
rect_1_fft = np.fft.fft(rect_pulse_1)
rect_1_amp = np.abs(rect_1_fft) * 2 / len(t)
rect_1_phase = np.angle(rect_1_fft)
# X(t - 3T/2)
rect_2_fft = np.fft.fft(rect_pulse_2)
rect_2_amp = np.abs(rect_2_fft) * 2 / len(t)
rect_2_phase = np.angle(rect_2_fft)
# X(t/2 - T/2)
rect_3_fft = np.fft.fft(rect_pulse_3)
rect_3_amp = np.abs(rect_3_fft) * 2 / len(t)
rect_3_phase = np.angle(rect_3_fft)
'''Frequency Bins'''
sampling_interval = t[1] - t[0]
rect_1_frequency_bins = np.fft.fftfreq(len(rect_pulse_1), d=sampling_interval)
rect_2_frequency_bins = np.fft.fftfreq(len(rect_pulse_2), d=sampling_interval)
rect_3_frequency_bins = np.fft.fftfreq(len(rect_pulse_3), d=sampling_interval)
# Plot the rectangular pulse
'''Time Domain'''
plt.figure(figsize=(10, 6))
plt.plot(t, rect_pulse_1)
plt.title(r'Rectangular Pulse-1: $X(t - T/2)$ - Time Domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.figure(figsize=(10, 6))
plt.plot(t, rect_pulse_2)
plt.title(r'Rectangular Pulse-2: $X(t - 3T/2)$ - Time Domain')
plt.xlabel('Time (s')
plt.ylabel('Amplitude')
plt.grid(True)
plt.figure(figsize=(10, 6))
plt.plot(t, rect_pulse_3)
plt.title(r'Rectangular Pulse-3: $X(t/2 - T/2)$ - Time Domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

'''Amplitude Spectrum'''
plt.figure(figsize=(10, 6))
plt.plot(rect_1_frequency_bins, rect_1_amp)
plt.title('Amplitude Spectrum Rectangular Pulse-1')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.figure(figsize=(10, 6))
plt.plot(rect_2_frequency_bins, rect_2_amp)
plt.title('Amplitude Spectrum Rectangular Pulse-2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.figure(figsize=(10, 6))
plt.plot(rect_3_frequency_bins, rect_3_amp)
plt.title('Amplitude Spectrum Rectangular Pulse-3')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)

'''Phase Spectrum'''
plt.figure(figsize=(10, 6))
plt.plot(rect_1_frequency_bins, rect_1_phase)
plt.title('Phase Spectrum Rectangular Pulse-1')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Radians)')
plt.grid(True)
plt.figure(figsize=(10, 6))
plt.plot(rect_2_frequency_bins, rect_2_phase)
plt.title('Phase Spectrum Rectangular Pulse-2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Radians)')
plt.grid(True)
plt.figure(figsize=(10, 6))
plt.plot(rect_3_frequency_bins, rect_3_phase)
plt.title('Phase Spectrum Rectangular Pulse-3')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Radians)')
plt.grid(True)

plt.tight_layout()
plt.show()
#AV