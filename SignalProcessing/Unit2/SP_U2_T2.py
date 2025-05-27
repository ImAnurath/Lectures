#Second Unit Task-2
import numpy as np
import matplotlib.pyplot as plt
'''
Do not flip unlike Convolution -> Shift the second -> Multiply with first -> Sum the results -> New Signal
'''
def rect(time, duration, amp):
    return amp * np.heaviside(time + duration/2, 1/2) - np.heaviside(time - duration/2, 1/2)

def right_triangular_pulse(time, duration, amp):
    return amp * np.piecewise(time, 
                        [time < 0, (time >= 0) & (time <= duration), time > duration],
                        [0, lambda t: 1 - t / duration, 0])

def cross_correlation(rect, tri):
    return np.correlate(rect, tri, mode='full')
'''Amplitudes'''
Ag = 1
Av = 1
'''Durations'''
duration_g = 6 #rect
duration_v = 3 #tri

discretization_frequency = 1e3
delta_t = 1 / discretization_frequency
time_interval = np.arange(-10, 10, delta_t)


pulse_rect = rect(time_interval, duration_g, Ag)
pulse_tri = right_triangular_pulse(time_interval, duration_v, Av)
cross = cross_correlation(pulse_rect, pulse_tri)
tau = np.arange(-len(time_interval) + 1, len(time_interval)) * delta_t # New time interval
'''Plotting'''
plt.figure(figsize=(14, 7))
plt.subplot(3, 1, 1)
plt.plot(time_interval, pulse_tri, label="Triangular Pulse", color='b')
plt.title("Right Triangular Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
#======================================
plt.subplot(3, 1 ,2)
plt.plot(time_interval, pulse_rect, label="Rectangular Pulse", color='g')
plt.title("Rect Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1 ,3)
plt.plot(tau, cross, label="Cross Correlation", color='r')
plt.title("Cross Correlation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout(pad= 2.0)
plt.show()