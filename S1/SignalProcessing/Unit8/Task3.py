import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
s = sp.symbols('s')

# Define the transfer function S(s) = (s^2) / (s^2 + 4s + 8) => (s+2)^2 + 4
numerator = s**2
denominator = s**2 + 4*s + 8

# Find the zeros (roots of the numerator)
zeros = sp.solve(numerator, s)
poles = sp.solve(denominator, s)
zeros = np.array([complex(z) for z in zeros])
poles = np.array([complex(p) for p in poles])
plt.figure(figsize=(6,6))
plt.scatter(zeros.real, zeros.imag, marker='o', color='red', label='Zeros')  # Zeros
plt.scatter(poles.real, poles.imag, marker='x', color='blue', label='Poles')  # Poles
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole-Zero Diagram')
plt.legend()
plt.grid(True)
plt.show()
