import tkinter as tk
from tkinter import filedialog, simpledialog
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
def select_audio_file():
    file_path = filedialog.askopenfilename(title="Select M02 noisy audio file",
                                           filetypes=[("WAV Files", "*.wav")])
    return file_path

def load_audio(file_path):
    sr, data = wav.read(file_path)
    if len(data.shape) > 1:  # Convert stereo to mono
        data = np.mean(data, axis=1)
    data = data.astype(np.float32) / np.max(np.abs(data))  # Normalize to float32
    return sr, data

def get_segment_times(signal_duration_ms):

    start_ms = simpledialog.askinteger("Input Noise Start Time",
                                        "Enter noise segment start time (ms):",
                                        minvalue=0, maxvalue=int(signal_duration_ms))

    end_ms = simpledialog.askinteger("Input Noise End Time",
                                        "Enter noise segment end time (ms):",
                                        minvalue=start_ms + 1, # End must be after start
                                        maxvalue=int(signal_duration_ms))
    return start_ms, end_ms

def frame_and_window(signal, sr, frame_duration=0.02):
    '''
    20 ms non-overlapping frames
    
    Idea is to create 2D arrays that are equally seperated in time. 
    length is 220 (First wav file) -> 220 splits, thats also why we need to pad the signal because of the possibility of a remainder value on the signal
    '''
    frame_length = int(sr * frame_duration)
    n_samples = len(signal)
    n_frames = int(np.ceil(n_samples / frame_length))
    
    '''
    Pad the signal to avoid errors
    '''
    pad_length = n_frames * frame_length - n_samples
    signal_padded = np.concatenate((signal, np.zeros(pad_length)))
    frames = np.reshape(signal_padded, (n_frames, frame_length))
    '''
    Hanning window function, then apply it to the frames
    '''
    window = np.hanning(frame_length)
    frames_windowed = frames * window
    return frames_windowed, frame_length


def task_3(sr, noisy_signal):
    '''
    Apply DFT to the windowed frames
    '''
    frames_windowed, frame_length = frame_and_window(noisy_signal, sr)
    dft_frames = np.fft.fft(frames_windowed, axis=1)
    magnitude_spectrum = np.abs(dft_frames)
    frequencies = np.fft.fftfreq(frame_length, d=1/sr)
    phase_spectrum = np.angle(dft_frames)
    return magnitude_spectrum, frequencies, frame_length, phase_spectrum

def task_4(X_k, G_k, phase_spectrum):
    alpha = 0.1  # Spectral floor scale
    estimated_mag = X_k - G_k
    estimated_mag = np.maximum(estimated_mag, alpha * G_k)  # Spectral floor

    # Smoothing
    smoothed_mag = np.copy(estimated_mag)
    for i in range(1, len(estimated_mag) - 1):
        smoothed_mag[i] = (estimated_mag[i-1] + estimated_mag[i] + estimated_mag[i+1]) / 3

    # Reconstruct time-domain signal
    enhanced_dft = smoothed_mag * np.exp(1j * phase_spectrum)
    time_domain_frames = np.fft.ifft(enhanced_dft, axis=1).real
    enhanced_signal = time_domain_frames.flatten()

    return enhanced_signal

def compute_snr(signal, noise):
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

'''
Task 1 - 2
noisy_signal => x(n)
'''
noise_file = select_audio_file()
sr, noisy_signal  = load_audio(noise_file) # x(n)
signal_duration_ms = (len(noisy_signal) / sr) * 1000
# start_ms, end_ms = get_segment_times(signal_duration_ms)
'''
Task 3
This is the DFT block on the schema
magnitude_spectrum => |X(k)|
'''
X_k, frequencies, frame_length, phase_spectrum = task_3(sr, noisy_signal)

'''
|G(k)| - Averaged amplitude spectrum of background noise
'''
noise_duration_sec = 0.4 # For all the wav files the noise at the beginning lasted at least 0.4 seconds
noise_samples = int(sr * noise_duration_sec)
noise_only_signal = noisy_signal[:noise_samples]
G_k_magnitude, _, _, _ = task_3(sr, noise_only_signal)
G_k = np.mean(G_k_magnitude, axis=0)

'''
Task 4 - PAPD 
'''
enhanced_signal = task_4(X_k, G_k, phase_spectrum)

'''
Task 5
'''
t_original = np.arange(len(noisy_signal)) / sr * 1000
t_enhanced = np.arange(len(enhanced_signal)) / sr * 1000

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t_original, noisy_signal)
plt.title("Original Noisy Signal")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(t_enhanced, enhanced_signal)
plt.title("Enhanced Signal (ŝ(n))")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

sf.write("enhanced_output.wav", enhanced_signal, sr)


'''
Task 7
'''
# Estimate noise using the same segment as before
noise_only_signal = noisy_signal[:noise_samples]
enhanced_noise_segment = enhanced_signal[:noise_samples]

speech_start_sec = 0.8  # Just like noise duration, but this is where roughly the speech starts on all the files
speech_duration_sec = 0.5 # How long the speech is, again its a rough estimation
speech_start = int(sr * speech_start_sec)
speech_end = speech_start + int(sr * speech_duration_sec)

noisy_speech_segment = noisy_signal[speech_start:speech_end]
enhanced_speech_segment = enhanced_signal[speech_start:speech_end]

# Compute SNRs
snr_noisy = compute_snr(noisy_speech_segment, noise_only_signal)
snr_enhanced = compute_snr(enhanced_speech_segment, enhanced_noise_segment)

print(f"SNR (Noisy): {snr_noisy:.2f} dB")
print(f"SNR (Enhanced): {snr_enhanced:.2f} dB")