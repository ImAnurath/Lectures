#Task 3
import numpy as np
import matplotlib.pyplot as plt

def rect(time):
    """Return a rectangular pulse of amplitude 1.0 between time -0.5 and 0.5,
    otherwise 0.0."""
    return np.where(np.abs(time) <= 0.5, 1.0, 0.0)

# Create time interval from -3 to 3 seconds, with 1000 steps
time_interval = np.linspace(-3, 3, 1000)

'''Copy paste of the equations''' 
s1 = (np.exp(-time_interval/2) * np.sin(10*np.pi*time_interval)) + (np.exp(-time_interval/3)*np.sin(15*np.pi*time_interval))
s2 = rect(time_interval) * 3 * np.cos(15 * np.pi * time_interval)
s3 = s1 - s2

'''s1 Plot'''
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.plot(time_interval, s1, label='$s_1(t)$', color='b')
plt.title('Signal $s_1(t)$: Sum of Decaying Harmonic Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
'''s2 Plot'''
plt.subplot(3, 1, 2)
plt.plot(time_interval, s2, label='$s_2(t)$', color='g')
plt.title('Signal $s_2(t)$: Rectangular Harmonic Pulse')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
'''s3 Plot'''
plt.subplot(3, 1, 3)
plt.plot(time_interval, s3, label='$s_3(t) = s_1(t) - s_2(t)$', color='r')
plt.title('Signal $s_3(t)$: Difference/Combined Signal(s)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

'''Two decaying harmonic signals are added. Without interruption they go to 0. However between -0.5 and 0.5 a rectangular pulse is applied. 
   which acts as a intensifier(???). '''
#AV
