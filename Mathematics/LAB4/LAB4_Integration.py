import numpy as np
from scipy.integrate import quad, trapezoid, simpson
def integrand_1(x):
    return x**3 - 2*x
def integrand_2(x):
    return np.sin(x)
def integrand_3(x):
    return np.exp(-x)
'''
Rombergs method is depricated from Scipy and is used as a base for quad. For all interval size 4 and 8 it is giving out same result. 
So I didn't included it on the for loop downbelow because it is using different abrevations 
'''
result_1 = 0
result_2 = 1
result_3 = 0.63212055883
rombergs_1, rombergs_error_1 = quad(integrand_1, 0, 2, limit = 4)
rombergs_2, rombergs_error_2 = quad(integrand_2, 0, np.pi/2, limit = 4)
rombergs_3, rombergs_error_3 = quad(integrand_3, 0, 1, limit = 4)

print(f"Exact result for integrand 1: {rombergs_1} (Error estimate: {rombergs_error_1})")
print(f"Exact result for integrand 2: {rombergs_2} (Error estimate: {rombergs_error_2})")
print(f"Exact result for integrand 3: {rombergs_3} (Error estimate: {rombergs_error_3})")

# Test the methods for different number of points (N) and different integrands
for N in [4, 8]:
    # Create the x values for the different integrands
    x_points = np.linspace(0, 2, N+1)  # For integrand 1 (0 to 2)
    x_points_2 = np.linspace(0, np.pi/2, N+1)  # For integrand 2 (0 to pi/2)
    x_points_3 = np.linspace(0, 1, N+1)  # For integrand 3 (0 to 1)

    # Iterate over the different integrands and calculate the integrals using the trapezoidal and simpson's method
    for i, (integrand, x_pts, exact_result) in enumerate([(integrand_1, x_points, result_1),
                                                           (integrand_2, x_points_2, result_2),
                                                           (integrand_3, x_points_3, result_3)], start=1):
        y_values = integrand(x_pts)
        trapezoidal = trapezoid(y_values, x_pts)
        simpsons = simpson(y_values, x=x_pts)
        print(f"Variant {i}:")
        print(f"  Trapezoidal Method: {trapezoidal} - Error: {abs(trapezoidal - exact_result)} - N: {N}")
        print(f"  Simpson's Method: {simpsons} - Error: {abs(simpsons - exact_result)} - N: {N}")
        print()

#####################################################
''' SECOND PART '''
import numpy as np
from scipy.integrate import quad, fixed_quad, simpson
from scipy.special import roots_hermite
import sympy as sp
def f(x):
    return np.sin(x)/x
def g(x):
    return np.exp(-x**2)

x = sp.Symbol('x')
exact_integral_1 = sp.integrate(sp.sin(x)/x, (x, 0, 100)).evalf()
exact_integral_2 = sp.integrate(sp.exp(-x**2), (x, 0, 100)).evalf()
''' evalf() is used to get the exact value of the integral 
with:    Simpson's Method": 0.675980982585610
without: Simpson's Method": -sqrt(pi)*erf(100)/2 + 1.56220790803837
'''
results_1 = {}
results_2 = {}
''' Simpson's Method '''
N = 200 # Points of integration
x_simpson = np.linspace(0.0000000001, 100, N) # 0.0000000001 to avoid division by 0
y_simpson_1 = f(x_simpson)
y_simpson_2 = f(x_simpson)
results_1["Simpson's Method"] = simpson(y_simpson_1, x = x_simpson)
results_2["Simpson's Method"] = simpson(y_simpson_2, x = x_simpson)

''' Adaptive Quadrature ''' #, epsabs is given by the paper
adaptive_integral_1, adaptive_integral_error_1 = quad(f, 0, 100, epsabs=1e-4) # These are numeric calculations so I can't use sympy
results_1["Adaptive Quadrature"] = adaptive_integral_1
adaptive_integral_2, adaptive_integral_error_2 = quad(g, 0, 100, epsabs=1e-4)
results_2["Adaptive Quadrature"] = adaptive_integral_2

''' quadl '''
adaptive_integral_1, adaptive_integral_error_1 = quad(f, 0, 100, epsabs=1e-4)
results_1["Quadl"] = adaptive_integral_1
adaptive_integral_2, adaptive_integral_error_2 = quad(g, 0, 100, epsabs=1e-4)
results_2["Quadl"] = adaptive_integral_2

''' Gauss-Hermite method 
    Since this method can be used on functions with e. Need to represent sinx/x with terms of e
    sinx/x = (e^jx - e^-jx) / 2j
    where j is the imaginary unit = sqrt(-1)
    I am just going to hard code the function into this type.
'''
def f_new(x):
    return (np.exp(x*1j) - np.exp(-x*1j)) / 2j
points, weights = roots_hermite(20)  # 20 gridpoints
results_1["Gauss-Hermite Method"] = np.sum(weights * f_new(points))
results_2["Gauss-Hermite Method"] =  np.sum(weights * g(points))
errors_1 = {method: abs(exact_integral_1 - value) for method, value in results_1.items()}
errors_2 = {method: abs(exact_integral_2 - value) for method, value in results_2.items()}

print(errors_1, "\n", errors_2)