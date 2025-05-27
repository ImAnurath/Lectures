import sympy as sp
import matplotlib.pyplot as plt

t, s = sp.symbols('t s')
x_t_neg = sp.exp(4 * t) * sp.Heaviside(-t)  # e^(4t) * u(-t)
x_t_pos = sp.exp(-6 * t) * sp.Heaviside(t)   # e^(-6t) * u(t)
# Laplace Transform of each part
X_s_neg = sp.laplace_transform(x_t_neg, t, s)
X_s_pos = sp.laplace_transform(x_t_pos, t, s)
X_s_total = sp.laplace_transform(x_t_neg + x_t_pos, t, s)


plt.figure(figsize=(10, 6))
plt.axvline(x=0, color='black', linewidth=1)
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=X_s_total[1], color='b', linestyle='--', label=f"Re(s) > {X_s_total[1]}") # We know that there is only 1 line so not gonna complicate the code
plt.fill_betweenx(y=[-10, 10], x1=int(X_s_total[1]), x2=10, color='blue', alpha=0.2)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.title("Region of Convergence (ROC) in the S-plane")
plt.legend()
plt.show()