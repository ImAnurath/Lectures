#Task1
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
def fix_frequencies(data1, data2, rate1, rate2):
    if rate1 > rate2:
        # Resample data1 to match data2's rate
        resampled = librosa.resample(data1, orig_sr=rate1, target_sr=rate2)
        rate1 = rate2
        return resampled, rate1, data2
    elif rate2 > rate1:
        # Resample data2 to match data1's rate
        resampled = librosa.resample(data2, orig_sr=rate2, target_sr=rate1)
        rate2 = rate1
        return resampled, rate2, data1
    else:
        # If the rates are already equal, no need to resample
        return data1, rate1, data2
def handle(data1, data2, rate1, rate2, mode):
    resampled, rate, data = fix_frequencies(data1, data2, rate1, rate2)
    convolved_signal = convolution(resampled, data, mode)
    convolved_time = set_time(convolved_signal, rate)
    return convolved_signal, convolved_time

'''Load Audio Files'''  
path = os.getcwd()
'''Load Chruch'''
wav_file_path = f'{path}\\SignalProcessing\\Unit6\\church_im.wav'
church_data, church_rate = librosa.load(wav_file_path, sr=None)
church_time = np.linspace(0, len(church_data) / church_rate, len(church_data)) # Time (x-axis) - for chruch
'''Load Dog Bark'''
wav_file_path = f'{path}\\SignalProcessing\\Unit6\\dog_bark_dry.wav'
dog_data, dog_rate = librosa.load(wav_file_path, sr=None)
dog_time = np.linspace(0, len(dog_data) / dog_rate, len(dog_data)) # Time (x-axis) - for dog

'''Fixing Frequencies'''
# Already Know Chruch Rate > Dog Rate but still
'''
same  -> same length as the longer input signal, centered with respect to the convolution.
valid -> only the part of the convolution where the signals overlap completely, but shorter
full  -> just gets everything
'''
mode = "full"
convolved_signal, convolved_time = handle(church_data, dog_data, church_rate, dog_rate, mode)
plt.figure(figsize=(10, 6))
plt.plot(convolved_time, convolved_signal)
plt.title("Convolved Signals")
plt.xlabel("Time [seconds]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
#AV