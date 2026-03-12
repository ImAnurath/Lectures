import numpy as np
import random
import matplotlib.pyplot as plt
'''
C = k1 * Fahrenheit + k2 => C = X*K
RLSE Equation:
K = (X^T * X + LAMDA * I)^-1 * X^T C
LAMBDA = Regularization Parameter
X = Inputs [Fahrenheit]
K = Coefficients [K1,K2]
'''
def rlse(X, Y, K, lamb):
    K = np.linalg.pinv(X.T @ X + lamb * np.eye(2)) @ X.T @ Y
    print(K)
    return K

temps_data = np.array([
    [13 , 55],
    [14 , 58],
    [17 , 63],
    [18 , 65],
    [19 , 66],
    [15 , 59],
    [13 , 56],
    [31 , 87],
    [32 , 90],
    [29 , 85],
    [27 , 81],
])
# Column of ones for bias terms
dum = np.ones((len(temps_data), 1))
# This part extracts Faghrenheit value array and reshapes it into a column vector
X = temps_data[:, 1].reshape(-1, 1)
# X is now Fahrenheit values and columns of 1 for bias
X = np.append(X, dum, axis=1)
# Celsius values
Y = temps_data[:, 0]
# Initial values for k1 and k2
k1 = random.uniform(0, 1)
k2 = random.uniform(0, 1)
K = np.array([k1, k2])

lamb = 0.01
actual_k1 = 0.5555555555555556 # 5/9
actual_k2 = -17.77777777777778 # -17 7/9
RLSE = rlse(X, Y, K, lamb)
print(f"{actual_k1} = {RLSE[0]}, {actual_k2} = {RLSE[1]}")
plt.figure(figsize=(10, 6))
plt.scatter(temps_data[:, 1], temps_data[:, 0])
plt.plot(temps_data[:, 1], RLSE[0] * temps_data[:, 1] + RLSE[1])
plt.show()


