#Second Unit Task-1
'''
I am assuming end result of this task should be the same as "signal composition 3#4" on our lecture document. 
However, I am not sure which, I couldnt flip the graph properly neither on y-axis. 
This is confusing...
'''

'''
Flip the second -> Shift the second -> Multiply with first -> Sum the results
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
def rect(time, duration, amp):
    return amp * np.heaviside(time + duration/2, 1/2) - np.heaviside(time - duration/2, 1/2)

def right_triangular_pulse(time, duration, amp):
    return amp * np.piecewise(time, 
                        [time < 0, (time >= 0) & (time <= duration), time > duration],
                        [0, lambda t: 1 - t / duration, 0])

def convolution(signal_1, signal_2, dt):
    return np.convolve(signal_1, signal_2, mode='full') * dt

'''Amplitudes'''
Ag = 1
Av = 1
'''Durations'''
duration_g = 6 #rect
duration_v = 3 #tri
time_interval = np.linspace(-6, 4, 1000)
'''Convolution Time = Signal_1_Time + Signal_2_Time - 1'''
new_time = np.linspace(time_interval[0] + time_interval[0], time_interval[-1] + time_interval[-1], len(time_interval) * 2 - 1)
dt = np.diff(time_interval)[0]
'''Pulses'''
pulse_rect = rect(time_interval, duration_g, Ag)
pulse_tri = right_triangular_pulse(time_interval, duration_v, Av)
pulse_conv = convolution(pulse_rect, pulse_tri,dt)
'''Plotting'''
plt.figure(figsize=(14, 7))
gs = gridspec.GridSpec(3, 2, width_ratios=[1, 2], height_ratios=[1, 1, 0.5])

plt.subplot(gs[1, 0])
plt.plot(time_interval, pulse_tri, label="Triangular Pulse", color='b')
plt.title("Right Triangular Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
#======================================
plt.subplot(gs[0, 0])
plt.plot(time_interval, pulse_rect, label="Rectangular Pulse", color='g')
plt.title("Rect Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
#======================================
plt.subplot(gs[:, 1])
plt.plot(time_interval, pulse_tri, label="Triangular Pulse", color='b')
plt.title("Right Triangular Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.plot(time_interval, pulse_rect, label="Rectangular Pulse", color='g')
plt.title("Rect Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.plot(new_time, pulse_conv,label="Convolution", color='r')
plt.title("Convolution")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout(pad= 2.0)
plt.show()
#AV