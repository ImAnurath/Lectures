#Third Unit Task-2
import numpy as np
import os
import matplotlib.pyplot as plt
path = os.getcwd()
data = np.loadtxt(f'{path}\\SignalProcessing\\Unit3\\sunspot.dat')
year = data[:, 0].astype(int)
values = data[:, 1]

first_50_years = year[:50]
first_50_values = values[:50]

fft_values = np.fft.fft(values)
frequency  = np.fft.fftfreq(len(values))

positive_freq_indices = frequency > 0
frequency = frequency[positive_freq_indices]
fft_magnitude = np.abs(fft_values[positive_freq_indices])
periods = 1 / frequency


print(fft_values)
plt.figure(figsize=(10, 6))
plt.subplot(2,1,1)
plt.plot(year, values, marker='o', linestyle='-', color='b')
plt.xlabel('Year')
plt.ylabel('Number of Sunspots')
plt.title('Sunspots in Individual Years')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(first_50_years, first_50_values, marker='o', linestyle='-', color='r')
plt.xlabel('Year')
plt.ylabel('Number of Sunspots')
plt.title('Change in Sunspots Over the First 50 Years')
plt.grid(True)

plt.figure(figsize=(10, 6))
plt.subplot(2,1,1)
plt.plot(frequency, fft_magnitude, marker='o', linestyle='-', color='b')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum of Sunspot Activity')
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(periods, fft_magnitude, marker='o', linestyle='-', color='b')
plt.xlabel('Period ')
plt.ylabel('Magnitude')
plt.title('Period of Sunspot Activity')
plt.grid(True)

plt.tight_layout(pad= 2.0)
plt.show()
#AV