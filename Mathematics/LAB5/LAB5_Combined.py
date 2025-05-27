import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sympy import symbols, Function, Eq, dsolve, Piecewise

# Analytical Solution
# Define symbolic variables and functions
t = symbols('t', real=True, positive=True)
Uout = Function('Uout')(t)
RC = 0.1

# Define the ODEs and solve
# For t <= 0.5 (Uin = 1)
ode1 = Eq(Uout.diff(t) + Uout/RC, 1/RC)
cond1 = {Uout.subs(t, 0): 0}  # Initial condition
Uout1 = dsolve(ode1, ics=cond1)

# For t > 0.5 (Uin = 0)
ode2 = Eq(Uout.diff(t) + Uout/RC, 0)
cond2 = {Uout.subs(t, 0.5): Uout1.rhs.subs(t, 0.5)}  # Continuity condition
Uout2 = dsolve(ode2, ics=cond2)

# Define a piecewise function for the analytical solution
Uout_analytical = Piecewise(
    (Uout1.rhs, t <= 0.5),
    (Uout2.rhs, t > 0.5)
)

# Generate analytical solution values
t_vals = np.linspace(0, 1, 100)
Uout_vals = np.array([Uout_analytical.subs(t, val).evalf() for val in t_vals], dtype=float)

# Numerical Solution
# Define the numerical ODE function
def numerical_ode(t, Uout):
    Uin = 1 if t <= 0.5 else 0
    return (Uin - Uout) / RC

# Solve the numerical ODE using solve_ivp
tspan = (0, 1)
Uout0 = [0]  # Initial condition
sol = solve_ivp(numerical_ode, tspan, Uout0, t_eval=t_vals)

# Plot Combined Results
plt.figure(figsize=(10, 6))
plt.plot(t_vals, Uout_vals, 'r-', linewidth=2, label='Analytical Solution')
plt.plot(sol.t, sol.y[0], 'b--', linewidth=2, label='Numerical Solution')
plt.xlabel('Time (t)')
plt.ylabel('Uout(t)')
plt.title('Analytical vs Numerical Solution')
plt.legend()
plt.grid(True)
plt.show()
