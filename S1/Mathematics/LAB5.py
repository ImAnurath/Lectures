import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Function
'''
Equation from the book so I can adabt it to my ODE
y'(t) + a y(t) = r where y(0) = 0
y(t) = (y0 - r/a)*exp(-a*t) + r/a 

y'(t) = Uout'(t)
r = Uin

For Analytical
Uout'(t) = (Uin - Uout(t))/tau

For Numerical
Uout(t + h) - Uout(t) = h * (Uin/tau - Uout(t)/tau)

Final equation for Euler's method:
ODE:      Uout(t + h) = Uout(t) + h * (Uin/tau - Uout(t)/tau),  Uout(0) = 0
t = 0,    Uout(0.01)  = 0 + 0.01 * (1/0.1 - 0/0.1) = 0.1
t = 0.01, Uout(0.02)  = 0.1 + 0.01 * (1/0.1 - 0.1/0.1) = 0.19
t = 0.02, Uout(0.03)  = 0.19 + 0.01 * (1/0.1 - 0.19/0.1) = 0.271 and so on until t = 0.5
t = 0.5,  Uout(0.51)  = 1 + 0.01 * (0/0.1 - 1/0.1) = 0.9 Starts to decay from here
t = 0.99, Uout(1)     = Uout(0.99) + 0.01 * (0/0.1 - Uout(0.99)/0.1) = 0

Uin = 1, Uout(0) = 0, t =[0, 0.5]
Uin = 0, Uout(0.5) = 1 , t = [0.5, 1]
'''

# Parameters
tau = 0.1
h = 0.01  # Step 
time = np.arange(0, 1+h, h)  # Time from 0 to 1 second
U_in = np.where(time <= 0.5, 1, 0)  # 1 for time <= 0.5, 0 for time > 0.5
U_out = np.zeros(len(time))  # Initialize U_out array
# U_out[0] = 0, initial condition

'''
Numerical Euler's Method
Algorithm goes as:
U_out(1) = U_out(0) + h * (U_in(1) / tau - U_out(0) / tau)
U_out(2) = U_out(1) + h * (U_in(2) / tau - U_out(1) / tau)
'''
for i in range(1, len(time)):
    #U_out[i] starts from index 1, since index 0 is the initial condition
    U_out[i] = U_out[i-1] + h * (U_in[i] / tau - U_out[i-1] / tau) # Implementation of line 23

'''
Analytical Solution
'''
def analytical_solution(t, tau): # For inital conditions
    if t <= 0.5:
        return 1 - np.exp(-t / tau)
    else:
        return (1 - np.exp(-0.5 / tau)) * np.exp(-(t - 0.5) / tau)
U_out_analytical = np.array([analytical_solution(t, tau) for t in time])

plt.plot(time, U_out, label="Uout Numerical")
plt.plot(time, U_out_analytical, label="Uout Analytical", linestyle='--', color='r')
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC Circuit Response")
plt.legend()
plt.grid()
plt.show()
