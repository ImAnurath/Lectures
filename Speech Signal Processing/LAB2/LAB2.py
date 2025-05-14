import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from tkinter import filedialog, simpledialog, messagebox
import tkinter as tk
import scipy.signal
from scipy.signal import find_peaks
def select_audio_file():
    file_path = filedialog.askopenfilename(title="Select an audio file", filetypes=[("WAV files", "*.wav")])
    return file_path
def energy(data, samplerate, frame_length=20, overlap_ratio=0.5):
    overlap = int(frame_length * overlap_ratio)
    step = frame_length - overlap
    energies = [np.sum(data[i:i + frame_length] ** 2) for i in range(0, len(data) - frame_length + 1, step)]
    times = np.arange(len(energies)) * step / samplerate * 1000
    plt.plot(times, energies)
    plt.xlabel("Time (ms)")
    plt.ylabel("Energy")
    plt.title("Energy Diagram")
    plt.grid(True)
    plt.show()
def signal(data, samplerate):
    channels = data.shape[1] if len(data.shape) > 1 else 1
    time = np.linspace(0, len(data) / samplerate * 1000, len(data))

    plt.figure(figsize=(10, 8))
    # plt.subplot(2, 1, 1)
    if channels == 2:
        plt.plot(time, data[:, 0], label='Left Channel')
        plt.plot(time, data[:, 1], label='Right Channel')
    else:
        plt.plot(time, data, label='Mono Channel')
        
    plt.title("Entire Audio Signal")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def zcr(data, samplerate, frame_length=20, overlap_ratio=0.5):
    overlap = int(frame_length * overlap_ratio)
    step = frame_length - overlap
    if len(data.shape) > 1:
        data = data[:, 0]
    zcr_values = []
    for start in range(0, len(data) - frame_length + 1, step):
        frame = data[start:start + frame_length]
        sign_changes = np.abs(np.sign(frame[1:]) - np.sign(frame[:-1]))
        zcr = np.sum(sign_changes) / (2 * frame_length)
        zcr_values.append(zcr)
    times = np.arange(len(zcr_values)) * step / samplerate * 1000
    plt.plot(times, zcr_values)
    plt.xlabel("Time (ms)")
    plt.ylabel("Zero-Crossing Rate")
    plt.title("ZCR Diagram")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def segment(data, samplerate):
    channels = data.shape[1] if len(data.shape) > 1 else 1
    time = np.linspace(0, len(data) / samplerate * 1000, len(data))  # Convert to milliseconds

    start_time = simpledialog.askfloat("Input", "Enter start time (ms):", minvalue=0, maxvalue=time[-1])
    end_time = simpledialog.askfloat("Input", "Enter end time (ms):", minvalue=start_time, maxvalue=time[-1])

    start_index = np.argmax(time >= start_time)
    end_index = np.argmax(time >= end_time)
    
    segment_time = time[start_index:end_index]
    segment_data = data[start_index:end_index]
    
    if channels == 2:
        segment_data = segment_data[:, 0]  # Use one channel if stereo

    # Plot the selected segment
    plt.figure(figsize=(10, 4))
    plt.plot(segment_time, segment_data, label='Audio Signal')
    plt.title(f"Segment from {start_time} ms to {end_time} ms")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()
    autocorrelation(segment_data, samplerate)
    plot_spectrogram(segment_data, samplerate)

def plot_spectrogram(data, samplerate):
    channels = data.shape[1] if len(data.shape) > 1 else 1
    plt.figure(figsize=(10, 4))
    frequencies, times, Sxx = scipy.signal.spectrogram(data[:, 0] if channels == 2 else data, samplerate)
    plt.pcolormesh(times * 1000, frequencies, 10 * np.log10(Sxx), shading='gouraud')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (ms)')
    plt.title('Spectrogram')
    plt.colorbar(label='Power (dB)')
    plt.show()
def autocorrelation(data, samplerate):
    ac_full = np.correlate(data, data, mode='full')
    ac = ac_full[len(ac_full) // 2:] # Positive Parts
    ac = ac / np.max(ac) # Normalization
    # TODO: Do these properly
    lags = np.arange(len(ac)) / samplerate * 1000  # Convert lags to milliseconds
    plt.figure(figsize=(10, 4))
    plt.plot(lags, ac)
    plt.xlabel("Lag (ms)")
    plt.ylabel("Normalized Autocorrelation")
    plt.title("Autocorrelation Function")
    plt.grid(True)
    plt.show()
    peaks, _ = find_peaks(ac)
    peaks = peaks[peaks > 0] # Remove 0 lags
    if peaks.size > 0:
        # Select the first peak after lag 0
        first_peak = peaks[0]
        # Estimate the fundamental frequency: f0 = samplerate / lag
        f0 = samplerate / first_peak
    print(f"Fundamental Frequency: {f0:.2f} Hz")

file_path = select_audio_file()
data, samplerate = sf.read(file_path)
signal(data, samplerate)
frame_length = int(samplerate * 20 / 1000) # 20 ms frame length
overlap_ratio = 0.5
energy(data, samplerate, frame_length, overlap_ratio)
zcr(data, samplerate, frame_length, overlap_ratio)
segment(data, samplerate)