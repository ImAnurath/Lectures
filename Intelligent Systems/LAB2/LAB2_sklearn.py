import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

x = np.linspace(0.1, 1, 20).reshape(-1, 1)
y = ((1 + 0.6 * np.sin(2 * np.pi * x / 0.7)) + 0.3 * np.sin(2 * np.pi * x)) / 2

mlp = MLPRegressor(hidden_layer_sizes=(6,), activation='tanh', solver='lbfgs', max_iter=1000, random_state=1)
mlp.fit(x, y.ravel())

y_pred = mlp.predict(x)

plt.scatter(x, y, color='blue', label='Actual')
plt.plot(x, y_pred, color='red', label='Predicted')
plt.xlabel('Input (x)')
plt.ylabel('Output (y)')
plt.legend()
plt.show()
