#Task2
import numpy as np
import matplotlib.pyplot as plt
'''
As the sample increase, for time domain it looks smoother and better. But I kept it low because it was making frequency domain hard to see.
For proper result you can change it to 1000
'''
t = np.linspace(0, 1, 1000) # 1 second, # samples
'''Values'''
A_1 = 1
A_2 = 1.5
A_3 = 1
f_1 = 20
f_2 = 45
f_3 = 65
w_1 = 2 * np.pi * f_1
w_2 = 2 * np.pi * f_2
w_3 = 2 * np.pi * f_3
# ======================================

''' Original Signal '''
original_signal = A_1 * np.cos(w_1 * t) + A_2 * np.cos(w_2 * t) + A_3 * np.cos(w_3 * t)
original_fft = np.fft.fft(original_signal)
original_fft_amplitude = np.abs(original_fft) * 2 / len(t)
original_sampling_interval = t[1] - t[0]
original_frequency_bins = np.fft.fftfreq(len(original_signal), d=original_sampling_interval) # Frequency bins
original_positive_indices = original_frequency_bins > 0 # Just to get rid of the negative symmetric part

# ======================================
def sample_fft(t, A_1, A_2, A_3, w_1, w_2, w_3, sample_frequency):
    new_t = np.arange(0, 1, 1/sample_frequency)
    new_sample = A_1 * np.cos(w_1 * new_t) + A_2 * np.cos(w_2 * new_t) + A_3 * np.cos(w_3 * new_t)
    new_sample_fft = np.fft.fft(new_sample)
    new_sample_fft_amplitude = np.abs(new_sample_fft) * 2 / len(t)
    new_sample_sampling_interval = new_t[1] - new_t[0]
    new_sample_frequency_bins = np.fft.fftfreq(len(new_sample), d=new_sample_sampling_interval)
    new_sample_positive_indices = new_sample_frequency_bins > 0
    return new_t, new_sample, new_sample_frequency_bins, new_sample_fft_amplitude, new_sample_positive_indices
def sample_reconstructed(t, A_1, A_2, A_3, w_1, w_2, w_3, sample_frequency):
    
    pass
'''First Sample at 140 Hz Constructed '''
first_sample_frequency = 140
t_first = np.arange(0, 1, 1/first_sample_frequency)
first_sample = A_1 * np.cos(w_1 * t_first) + A_2 * np.cos(w_2 * t_first) + A_3 * np.cos(w_3 * t_first)
first_sample_fft = np.fft.fft(first_sample)
first_sample_fft_amplitude = np.abs(first_sample_fft) * 2 / len(t)
first_sample_sampling_interval = t_first[1] - t_first[0]
first_sample_frequency_bins = np.fft.fftfreq(len(first_sample), d=first_sample_sampling_interval)
first_sample_positive_indices = first_sample_frequency_bins > 0
first_reconstructed_signal = np.interp(t, t_first, first_sample) # Resconstruct the signal for time domain
'''FFT of reconstructed signals for Amplitude spectra'''
first_reconstructed_fft = np.fft.fft(first_reconstructed_signal)
first_reconstructed_fft_amplitude = np.abs(first_reconstructed_fft) * 2 / len(t)
first_reconstructed_frequency_bins = np.fft.fftfreq(len(first_reconstructed_signal), d=(t[1] - t[0]))
first_reconstructed_positive_indices = first_reconstructed_frequency_bins > 0
# ======================================        

'''Second Sample at 120  Hz Constructed '''
second_sample_frequency = 120
t_second = np.arange(0, 1, 1/second_sample_frequency)
second_sample = A_1 * np.cos(w_1 * t_second) + A_2 * np.cos(w_2 * t_second) + A_3 * np.cos(w_3 * t_second)
second_sample_fft = np.fft.fft(second_sample)
second_sample_fft_amplitude = np.abs(second_sample_fft) * 2 / len(t)
second_sample_sampling_interval = t_second[1] - t_second[0]
second_sample_frequency_bins = np.fft.fftfreq(len(second_sample), d=second_sample_sampling_interval)
second_sample_positive_indices = second_sample_frequency_bins > 0
second_reconstructed_signal = np.interp(t, t_second, second_sample) # Resconstruct the signal for time domain
'''FFT of reconstructed signals for Amplitude spectra'''
second_reconstructed_fft = np.fft.fft(second_reconstructed_signal)
second_reconstructed_fft_amplitude = np.abs(second_reconstructed_fft) * 2 / len(t)
second_reconstructed_frequency_bins = np.fft.fftfreq(len(second_reconstructed_signal), d=(t[1] - t[0]))
second_reconstructed_positive_indices = second_reconstructed_frequency_bins > 0
# ======================================

'''Third Sample at 80  Hz Constructed'''
third_sample = 80
t_third = np.arange(0, 1, 1/third_sample)
third_sample = A_1 * np.cos(w_1 * t_third) + A_2 * np.cos(w_2 * t_third) + A_3 * np.cos(w_3 * t_third)
third_sample_fft = np.fft.fft(third_sample)
third_sample_fft_amplitude = np.abs(third_sample_fft) * 2 / len(t)
third_sample_sampling_interval = t_third[1] - t_third[0]
third_sample_frequency_bins = np.fft.fftfreq(len(third_sample), d=third_sample_sampling_interval)
third_sample_positive_indices = third_sample_frequency_bins > 0
third_reconstructed_signal = np.interp(t, t_third, third_sample) # Resconstruct the signal for time domain
'''FFT of reconstructed signals for Amplitude spectra'''
third_reconstructed_fft = np.fft.fft(third_reconstructed_signal)
third_reconstructed_fft_amplitude = np.abs(third_reconstructed_fft) * 2 / len(t)
third_reconstructed_frequency_bins = np.fft.fftfreq(len(third_reconstructed_signal), d=(t[1] - t[0]))
third_reconstructed_positive_indices = third_reconstructed_frequency_bins > 0
# ======================================

'''Plotting'''

'''Original Signal'''
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, original_signal, label="Original Signal in Time Domain", color='b')
plt.title("Original Signal in Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(original_frequency_bins[original_positive_indices], original_fft_amplitude[original_positive_indices],label="Original Signal in Frequency Domain", color='b')
plt.title("Original Signal in Frequency Domain")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout(pad= 3.0)
# ======================================

'''First Sample 140Hz'''
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t_first, first_sample, label="First Sample Signal(140 Hz) in Time Domain", color='b')
plt.title("First Sample Signal(140 Hz) in Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(first_sample_frequency_bins[first_sample_positive_indices], first_sample_fft_amplitude[first_sample_positive_indices],label="First Sample Signal(140 Hz) in Frequency Domain", color='b')
plt.title("First Sample Signal(140 Hz) in Frequency Domain")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout(pad= 3.0)
# ======================================

'''Second Sample Sample 120Hz'''
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t_second, second_sample, label="Second Sample Signal(120 Hz) in Time Domain", color='b')
plt.title("Second Sample Signal(120 Hz) in Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(second_sample_frequency_bins[second_sample_positive_indices], second_sample_fft_amplitude[second_sample_positive_indices],label="Second Sample Signal(120 Hz) in Frequency Domain", color='b')
plt.title("Second Sample Signal(120 Hz) in Frequency Domain")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout(pad= 3.0)
# ======================================

'''Third Sample Sample 120Hz'''
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t_third, third_sample, label="Third Sample Signal(80 Hz) in Time Domain", color='b')
plt.title("Third Sample Signal(80 Hz) in Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(third_sample_frequency_bins[third_sample_positive_indices], third_sample_fft_amplitude[third_sample_positive_indices],label="Third Sample Signal(80 Hz) in Frequency Domain", color='b')
plt.title("Third Sample Signal(80 Hz) in Frequency Domain")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout(pad= 3.0)
# ======================================
'''Comparisions'''
# Timing diagrams
plt.figure(figsize=(10, 6))
'''First Comparison'''
plt.subplot(3, 1, 1)
plt.plot(t, original_signal, label='Original Signal', color='b', linestyle='--')
plt.plot(t, first_reconstructed_signal, label='Reconstructed Signal(140 Hz)', color='r', linestyle='-')
plt.title("Timing Diagram: Original vs Reconstructed Signal(140 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
'''Second Comparison'''
plt.subplot(3, 1, 2)
plt.plot(t, original_signal, label='Original Signal', color='b', linestyle='--')
plt.plot(t, second_reconstructed_signal, label='Reconstructed Signal(120 Hz)', color='r', linestyle='-')
plt.title("Timing Diagram: Original vs Reconstructed Signal(120 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
'''Third Comparison'''
plt.subplot(3, 1, 3)
plt.plot(t, original_signal, label='Original Signal', color='b', linestyle='--')
plt.plot(t, third_reconstructed_signal, label='Reconstructed Signal(80 Hz)', color='r', linestyle='-')
plt.title("Timing Diagram: Original vs Reconstructed Signal(80 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout(pad= 3.0)
# ======================================
# Amplitude spectra
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(original_frequency_bins[original_positive_indices], original_fft_amplitude[original_positive_indices],label='Original Signal Spectrum', color='b', linestyle='--')
plt.plot(first_reconstructed_frequency_bins[first_reconstructed_positive_indices], first_reconstructed_fft_amplitude[first_reconstructed_positive_indices],label='Reconstructed Signal Spectrum (140 Hz)', color='r', linestyle='-')
plt.title("Amplitude Spectra: Original vs Reconstructed Signal (140 Hz)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.subplot(3, 1, 2)
plt.plot(original_frequency_bins[original_positive_indices], original_fft_amplitude[original_positive_indices],label='Original Signal Spectrum', color='b', linestyle='--')
plt.plot(second_reconstructed_frequency_bins[second_reconstructed_positive_indices], second_reconstructed_fft_amplitude[second_reconstructed_positive_indices],label='Reconstructed Signal Spectrum (120 Hz)', color='r', linestyle='-')
plt.title("Amplitude Spectra: Original vs Reconstructed Signal (120 Hz)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.subplot(3, 1, 3)
plt.plot(original_frequency_bins[original_positive_indices], original_fft_amplitude[original_positive_indices],label='Original Signal Spectrum', color='b', linestyle='--')
plt.plot(third_reconstructed_frequency_bins[third_reconstructed_positive_indices], third_reconstructed_fft_amplitude[third_reconstructed_positive_indices],label='Reconstructed Signal Spectrum (80 Hz)', color='r', linestyle='-')
plt.title("Amplitude Spectra: Original vs Reconstructed Signal(80 Hz)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
#AV