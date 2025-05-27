# IS LAB2-Extra
import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

x1 = np.linspace(0, 1, 20)
x2 = np.linspace(0, 1, 20)
# Create a 2D grid with x1 and x2 as the axes
x1, x2 = np.meshgrid(x1, x2)
# Create input features by flattening the grid
X = np.c_[x1.ravel(), x2.ravel()]

# Define the target function and flatten it
y = (np.sin(np.pi * x1) * np.cos(np.pi * x2)).ravel()

# Initialize a Multi-layer Perceptron Regressor
mlp = MLPRegressor(
    hidden_layer_sizes=(10,),  # Single hidden layer with 10 neurons
    activation='tanh',         # Use 'tanh' as the activation function
    solver='lbfgs',            # Use 'lbfgs' solver for optimization
    max_iter=1000,             # Maximum iterations for convergence
    random_state=1             # Random state for reproducibility
)

# Fit the model to the data
mlp.fit(X, y)

y_pred = mlp.predict(X)
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x1, x2, y.reshape(x1.shape), cmap='viridis')
ax1.set_title('Actual Surface')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x1, x2, y_pred.reshape(x1.shape), cmap='viridis')
ax2.set_title('Predicted Surface')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('y_pred')

plt.show()
