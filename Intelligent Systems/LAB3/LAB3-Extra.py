#LAB3-EXTRA
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

# Input and desired output
x = np.linspace(0.1, 1, 20)  # Input generation
y = (1 + 0.6 * np.sin(2 * np.pi * x / 0.7) + 0.3 * np.sin(2 * np.pi * x)) / 2  # Desired output

# Fit an RBF model (automatically finds centers and radii)
rbf = Rbf(x, y, function='gaussian')  # 'gaussian' is the RBF kernel

# Predict output for the input values
y_pred = rbf(x)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo-', label="Desired Output")
plt.plot(x, y_pred, 'r--', label="RBF Network Output")
plt.title("RBF Network Approximation (Using scipy.interpolate.Rbf)")
plt.xlabel("Input (x)")
plt.ylabel("Output (y)")
plt.legend()
plt.grid(True)
plt.show()

# Access RBF centers
print("RBF Centers (Nodes):", rbf.nodes)  # Print centers (c1, c2, etc.)

# If you want to estimate the radii, you can calculate the distances between centers
distances = np.diff(rbf.nodes.flatten())  # Distance between consecutive centers
print("RBF Center Distances (Approximated Radii):", distances)
#AV