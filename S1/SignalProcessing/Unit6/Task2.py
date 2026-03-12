#Task2
import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
def set_time(convolved_signal, sample_rate):
    duration = len(convolved_signal) / sample_rate  # Total duration in seconds
    time_vector = np.linspace(0, duration, len(convolved_signal))  # Create time vector
    return time_vector
def convolution(signal1, signal2, mode ="full"):
    # Perform convolution of the two signals
    return np.convolve(signal1, signal2, mode=mode)
def compute_spectrum(signal, sample_rate):
    spectrum = np.fft.fft(signal)
    # Calculate the frequency axis
    frequencies = np.fft.fftfreq(len(spectrum), d=1/sample_rate)
    # Get the magnitude spectrum (only the positive frequencies)
    magnitude_spectrum = np.abs(spectrum)
    return frequencies, magnitude_spectrum
def plot_frequency_spectrum(frequencies, magnitude_spectrum, title):
    plt.figure(figsize=(10, 5))
    plt.plot(frequencies[:len(frequencies)//2], magnitude_spectrum[:len(magnitude_spectrum)//2])  # Only plot positive frequencies
    plt.title(title)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.xlim(0, max(frequencies) / 2)  # Limit x-axis to positive frequencies
    plt.show()
def plot_time_spectrum(amplitude, time, title):
    plt.figure(figsize=(10, 5))
    plt.plot(time, amplitude)
    plt.title(title)
    plt.xlabel("Time [seconds]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
'''Load Audio Files'''  
path = os.getcwd()
'''Load Chruch'''
wav_file_path = f'{path}\\SignalProcessing\\Unit6\\female4_clean_16k.wav'
female_data, female_rate = librosa.load(wav_file_path, sr=None)
female_time = np.linspace(0, len(female_data) / female_rate, len(female_data)) # Time (x-axis) - for chruch
'''Load Dog Bark'''
wav_file_path = f'{path}\\SignalProcessing\\Unit6\\Scena_echo.wav'
scena_data, scena_rate = librosa.load(wav_file_path, sr=None)
scena_time = np.linspace(0, len(scena_data) / scena_rate, len(scena_data)) # Time (x-axis) - for dog

''' Transform to Frequency Domain'''
female_frequency, female_magnitude = compute_spectrum(female_data, female_rate)
scena_frequency,  scena_magnitude  = compute_spectrum(scena_data, scena_rate)

''' ACTION SEQUENCE '''

''' 1- Signals in Time Domain'''
plot_time_spectrum(female_data, female_time, "Female Signal in Time")
plot_time_spectrum(scena_data, scena_time,   "Scena Signal in Time")

''' 2- Signals in Frequency Domain (Spectra)'''
plot_frequency_spectrum(female_frequency, female_magnitude, "Female Signal in Frequency")
plot_frequency_spectrum(scena_frequency,  scena_magnitude,  "Scena Signal in Frequency")

''' 3- Already Determined the sampling rates on Load'''

''' 4- Resampling the signlas to the same rate'''
# Since action 5 wants both signals convolution, I am going to hard code it.
# Higher to Lower
# 96000 Hz to 16000 Hz
resampled_signal1 = librosa.resample(scena_data, orig_sr=scena_rate, target_sr=female_rate)
# Lower to Higher
# 16000 Hz to 96000 Hz
resampled_signal2 = librosa.resample(female_data, orig_sr=female_rate, target_sr=scena_rate)

''' 5- Perfom Convolution on Signals'''
convolution_signal1 = convolution(resampled_signal1, resampled_signal2)
convolution_signal2 = convolution(resampled_signal2, resampled_signal1)
''' 6- Plotting Convolution signal in Time'''
# It is the same but still.
conv_signal1_time = set_time(convolution_signal1, female_rate) # Target Frequency is female_rate
conv_signal2_time = set_time(convolution_signal2, scena_rate) # Target Frequency is scena_rate
plot_time_spectrum(convolution_signal1, conv_signal1_time, "Convolution of Female Frequency(16000 Hz) to Scena Frequency (96000 Hz) in Time")
plot_time_spectrum(convolution_signal2, conv_signal2_time , "Convolution of Scena Frequency (96000 Hz) to Female Frequency(16000 Hz) in Time")
''' 7- Plotting Convolution signal in Frequency'''
# Since convolution_1 = convolution_2 I am just going to use one of them to reduce clutter.
convolution_signal1_frequency, convolution_signal1_magnitude = compute_spectrum(convolution_signal1, female_rate)
convolution_signal2_frequency, convolution_signal2_magnitude = compute_spectrum(convolution_signal2, scena_rate)
plot_frequency_spectrum(convolution_signal1_frequency, convolution_signal1_magnitude, "Convolution Signal In Frequency")
#AV