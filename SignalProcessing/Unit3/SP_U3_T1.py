#Third Unit Task-1
import os
import librosa
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
import soundfile as sf
path = os.getcwd()

# Load the .wav file
wav_file_path = f'{path}\\SignalProcessing\\Unit3\\bluewhale_with_noise.wav'
data_noise, rate_noise = librosa.load(wav_file_path, sr=None)  # Load with original sampling rate
# Load the .au file
au_file_path = f'{path}\\SignalProcessing\\Unit3\\bluewhale.au'
data_original, rate_original = librosa.load(au_file_path, sr=None)  # Load with original sampling rate


time_noise = np.linspace(0, len(data_noise) / rate_noise, num=len(data_noise)) # Time (x-axis) of with noise 
time_original = np.linspace(0, len(data_original) / rate_original, num=len(data_original)) # Time (x-axis) of original

# Normalize AMP
data_noise = data_noise / np.max(np.abs(data_noise))
data_original = data_original / np.max(np.abs(data_original))

# Fourier Transform
fft_original = np.fft.fft(data_original) #Time domain to frequency domain
frequencies = np.fft.fftfreq(len(fft_original), d=1/rate_original) #Frequency of the new domain, replaces x-axis

# Added new noise
data_with_noise = data_original + 1.5 * np.sin(2 * np.pi * 120 * time_original)
data_with_noise = data_with_noise / np.max(np.abs(data_with_noise)) # Normalize new noisy signal
fft_new = np.fft.fft(data_with_noise)
new_freq = np.fft.fftfreq(len(fft_new), d=1/rate_original)

#Filtering
cutoff_frequency = 100
filter_mask = np.abs(new_freq) < cutoff_frequency
filtered_fft = fft_new * filter_mask # Mask applying
filtered_signal = np.fft.ifft(filtered_fft) #Changing it back to time domain

# Exporting
from scipy.io.wavfile import write

# Ensure the filtered signal is real and normalized
filtered_signal_real = np.real(filtered_signal)  # Take the real part if necessary
filtered_signal_normalized = filtered_signal_real / np.max(np.abs(filtered_signal_real))  # Normalize

# Specify the output file path
output_wav_path = 'filtered_signal.wav'

# Write the WAV file
write(output_wav_path, rate_original, (filtered_signal_normalized * 32767).astype(np.int16))  # Scale to int16

'''Plotting'''
# Plot the .wav signal (with noise)
# It looks flat out rectangle tho it is not when zoomed in
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time_noise, data_noise)
plt.title("Audio with Noise in Time Domain (.wav file)")
plt.xlabel("Time [seconds]")
plt.ylabel("Normalized Amplitude")
plt.grid(True)
plt.tight_layout(pad= 3.0)
# Plot the .au signal (original)
plt.subplot(2, 1, 2)
plt.plot(time_original, data_original)
plt.title("Original Audio in Time Domain (.au file)")
plt.xlabel("Time [seconds]")
plt.ylabel("Normalized Amplitude")
plt.grid(True)

# Original on Frequency domain
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(frequencies , fft_original)
plt.title("Signal Spectrum of Original Audio (.au file)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout(pad= 3.0)
plt.subplot(2, 1, 2)
plt.plot(time_original , data_with_noise)
plt.title("Original with Noise in Time Domain")
plt.xlabel("Time [seconds]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.figure(figsize=(10, 6))
# Better visualization?
plt.plot(new_freq , np.log10(np.abs(fft_new)))
plt.title("New Noisy Signal in Frequency Domain")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)

# ==============
# Looks like a mess with log10 but otherwise it is not clear :'')
plt.figure(figsize=(10, 6))
plt.plot(new_freq, np.log10(np.abs(fft_original)), label="Original Spectrum", color='b')
plt.plot(new_freq, np.log10(np.abs(fft_new)), label="Noisy Spectrum", color='r', alpha=0.7)
plt.title("Frequency-Domain Spectra")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)


plt.figure(figsize=(15, 15))
plt.subplot(3, 1, 1)
plt.plot(time_noise, data_noise)
plt.title("Audio with Noise in Time Domain (.wav file)")
plt.xlabel("Time [seconds]")
plt.ylabel("Normalized Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(time_original, data_original)
plt.title("Original Audio in Time Domain (.au file)")
plt.xlabel("Time [seconds]")
plt.ylabel("Normalized Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time_original, filtered_signal, label="Filtered Signal", color='g')
plt.title("Masked New Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)


plt.tight_layout(pad= 2.0)
plt.show()
#AV