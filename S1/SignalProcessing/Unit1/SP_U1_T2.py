#Task2
import numpy as np
import matplotlib.pyplot as plt

# Heaviside function
def rect(time, duration):
    return np.heaviside(time + duration/2, 1/2) - np.heaviside(time - duration/2, 1/2)

amp = 3
duration = 3 #Duration
t_start = -5
t_end = 5
time_interval = np.linspace(t_start, t_end, 1000)
pulse = amp * rect(time_interval, duration)

'''Plotting'''
plt.figure(figsize=(7, 5))
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.plot(time_interval, pulse)
plt.title('Rectangular Pulse Signal')
plt.grid(True)
plt.xlim(t_start, t_end)
plt.ylim(-0.1, amp + 0.1)
plt.show()
#AV