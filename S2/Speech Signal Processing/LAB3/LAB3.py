import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import scipy.signal as signal
import scipy.fftpack as fft
import librosa
import librosa.display
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog

def select_audio_file():
    file_path = filedialog.askopenfilename(title="Select an audio file - Order: Background -> Voiced -> Unvoiced",
                                           filetypes=[("WAV Files", "*.wav")])
    return file_path

def load_audio(file_path):
    sr, data = wav.read(file_path)
    if len(data.shape) > 1:  # Convert stereo to mono
        data = np.mean(data, axis=1)
    data = data.astype(np.float32) / np.max(np.abs(data))  # Normalize to float32
    return sr, data

def get_segment_times():
    root = tk.Tk()
    root.withdraw()
    start_ms = simpledialog.askinteger("Input", "Enter segment start time (ms):", minvalue=0)
    end_ms = simpledialog.askinteger("Input", "Enter segment end time (ms):", minvalue=start_ms + 1)
    return start_ms, end_ms

def plot_waveform(ax, data, sr, title):
    time_axis = np.linspace(0, len(data) / sr, num=len(data)) * 1000  # Convert to ms
    ax.plot(time_axis, data)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.grid()

def plot_spectrum(ax, segment, sr, title):
    N = len(segment)
    freq_axis = np.fft.rfftfreq(N, d=1/sr) / 1000  # Convert Hz to kHz
    spectrum = np.abs(np.fft.rfft(segment))
    
    ax.plot(freq_axis, spectrum)
    ax.set_xlabel("Frequency (kHz)")
    ax.set_ylabel("Magnitude")
    ax.set_title(title)
    ax.grid()

def extract_segment(data, sr, start_ms, end_ms):
    start_sample = int((start_ms / 1000) * sr)
    end_sample = int((end_ms / 1000) * sr)
    segment = data[start_sample:end_sample]
    return segment

def plot_cepstrum(ax, segment, sr, title):
    spectrum = np.log(np.abs(np.fft.rfft(segment)) + 1e-10)  # Avoid log(0)
    cepstrum = np.abs(np.fft.irfft(spectrum))
    quefrency_axis = np.arange(len(cepstrum)) / sr * 1000  # Convert to ms
    ax.plot(quefrency_axis, cepstrum)
    ax.set_xlabel("Quefrency (ms)")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.grid()

def plot_spectrogram(ax, data, sr, title):
    S = librosa.stft(data)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
    img = librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log', ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel("Frequency")
    ax.grid()

def estimate_fundamental_frequency(segment, sr):
    spectrum = np.log(np.abs(np.fft.rfft(segment)) + 1e-10)
    cepstrum = np.abs(np.fft.irfft(spectrum))
    min_cepstral_idx = int(sr / 500)
    max_cepstral_idx = int(sr / 50)
    peak_idx = np.argmax(cepstrum[min_cepstral_idx:max_cepstral_idx]) + min_cepstral_idx
    fundamental_frequency = sr / peak_idx
    return fundamental_frequency

print("Please Select in order: Background -> Voiced -> Unvoiced")
'''
Handle files
'''
background_file = select_audio_file()
voiced_file = select_audio_file()
unvoiced_file = select_audio_file()

sr_bg, data_bg = load_audio(background_file)
sr_voiced, data_voiced = load_audio(voiced_file)
sr_unvoiced, data_unvoiced = load_audio(unvoiced_file)


'''
Grid for plots
'''
fig, axs = plt.subplots(3, 4, figsize=(16, 12))  # 3 rows, 4 columns

'''
User input for ms segmentation
'''
start_ms, end_ms = get_segment_times()
seg_bg = extract_segment(data_bg, sr_bg, start_ms, end_ms)
seg_voiced = extract_segment(data_voiced, sr_voiced, start_ms, end_ms)
seg_unvoiced = extract_segment(data_unvoiced, sr_unvoiced, start_ms, end_ms)

'''
Task 1 - Speech Signal waveform in milliseconds
'''
plot_waveform(axs[0, 0], data_bg, sr_bg, "Background Noise Waveform")
plot_waveform(axs[0, 1], data_voiced, sr_voiced, "Voiced Sound Waveform")
plot_waveform(axs[0, 2], data_unvoiced, sr_unvoiced, "Unvoiced Sound Waveform")

'''
Task 2 - Speech Signal
'''
plot_spectrum(axs[1, 0], seg_bg, sr_bg, "Background Noise Spectrum")
plot_spectrum(axs[1, 1], seg_voiced, sr_voiced, "Voiced Sound Spectrum")
plot_spectrum(axs[1, 2], seg_unvoiced, sr_unvoiced, "Unvoiced Sound Spectrum")

plot_cepstrum(axs[2, 0], seg_bg, sr_bg, "Background Noise Cepstrum")
plot_cepstrum(axs[2, 1], seg_voiced, sr_voiced, "Voiced Sound Cepstrum")
plot_cepstrum(axs[2, 2], seg_unvoiced, sr_unvoiced, "Unvoiced Sound Cepstrum")


'''
Task 5 - Fundamental Frequency with cepstal
'''
f0_bg = estimate_fundamental_frequency(seg_bg, sr_bg)
f0_voiced = estimate_fundamental_frequency(seg_voiced, sr_voiced)
f0_unvoiced = estimate_fundamental_frequency(seg_unvoiced, sr_unvoiced)

print(f"Fundamental Frequency (Background): {f0_bg:.2f} Hz")
print(f"Fundamental Frequency (Voiced): {f0_voiced:.2f} Hz")
print(f"Fundamental Frequency (Unvoiced): {f0_unvoiced:.2f} Hz")

plot_spectrogram(axs[0, 3], data_bg, sr_bg, "Background Spectrogram")
plot_spectrogram(axs[1, 3], data_voiced, sr_voiced, "Voiced Spectrogram")
plot_spectrogram(axs[2, 3], data_unvoiced, sr_unvoiced, "Unvoiced Spectrogram")

plt.tight_layout()
plt.show()
