# LAB-1
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from tkinter import Tk, filedialog, simpledialog, messagebox

# %% Handle File
def select_audio_file():
    file_path = filedialog.askopenfilename(title="Select an audio file", filetypes=[("WAV files", "*.wav")])
    return file_path

def save_audio_file(data, samplerate):
    file_path = filedialog.asksaveasfilename(title="Save the audio segment", defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    if file_path:
        sf.write(file_path, data, samplerate)
#%%
def plot_audio_signal(file_path):
    # Read the audio file
    data, samplerate = sf.read(file_path) 
    channels = data.shape[1] if len(data.shape) > 1 else 1
    bits_per_sample = sf.info(file_path).subtype

    # Display audio file information
    print(f"Sampling Rate: {samplerate} Hz")
    print(f"Number of Channels: {channels}")
    print(f"Quantization Bits: {bits_per_sample}")

    # Create time axis in milliseconds
    time = np.linspace(0, len(data) / samplerate * 1000, len(data))

    # Plot the entire signal
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    # %% Plot the whole signal.
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
    # %% Segmenting the signal with inputs

    start_time = simpledialog.askfloat("Input", "Enter start time (ms):", minvalue=0, maxvalue=time[-1])
    end_time = simpledialog.askfloat("Input", "Enter end time (ms):", minvalue=start_time, maxvalue=time[-1])

    # Split the data into segments
    start_index = np.argmax(time >= start_time)
    end_index = np.argmax(time >= end_time)
    # %%
    
    # Plot the selected segment
    plt.subplot(2, 1, 2)
    
    segment_time = time[start_index:end_index]
    segment_data = data[start_index:end_index]
    
    if channels == 2:
        plt.plot(segment_time, segment_data[:, 0], label='Left Channel')
        plt.plot(segment_time, segment_data[:, 1], label='Right Channel')
    else:
        plt.plot(segment_time, segment_data, label='Mono Channel')
    
    plt.title(f"Audio Signal Segment from {start_time} ms to {end_time} ms")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.legend(loc='upper right')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

    # Handle the segment save
    if messagebox.askyesno("Save Segment", "Do you want to save the selected segment?"):
        save_audio_file(data[start_index:end_index], samplerate)
#%% Main
def main():
    file_path = select_audio_file()
    if file_path:
        plot_audio_signal(file_path)

if __name__ == "__main__":
    main()
#AV