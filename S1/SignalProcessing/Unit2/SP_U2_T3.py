#Second Unit Task-2
import numpy as np
import matplotlib.pyplot as plt
'''
Operations are same for as Cross Correlation just the same signals
'''
def right_triangular_pulse(time, duration, amp):
    return amp * np.piecewise(time, 
                        [time < 0, (time >= 0) & (time <= duration), time > duration],
                        [0, lambda t: 1 - t / duration, 0])

def auto_correlation(tri):
    return np.correlate(tri, tri, mode='full')

'''Amplitudes'''
Av = 2
'''Durations'''
duration_v = 3 #tri
'''Time'''
discretization_frequency = 1e3
delta_t = 1 / discretization_frequency
time_interval = np.arange(-10, 10, delta_t)

'''Pulse'''
pulse_tri = right_triangular_pulse(time_interval, duration_v, Av)
auto = auto_correlation(pulse_tri)
tau = np.arange(-len(time_interval) + 1, len(time_interval)) * delta_t # New time interval
'''Plotting'''
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
plt.plot(time_interval, pulse_tri, label="Triangular Pulse", color='b')
plt.title("Right Triangular Pulse")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
#======================================
plt.subplot(2, 1 ,2)
plt.plot(tau, auto, label="Auto Correlation", color='r')
plt.title("Aross Correlation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout(pad= 2.0)
plt.show()