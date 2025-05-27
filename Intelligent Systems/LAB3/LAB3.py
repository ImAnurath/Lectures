import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.1, 1, 20) # Input generation
# actual outputs = (1 + 0.6 * sin (2 * pi * x / 0.7)) + 0.3 * sin (2 * pi * x)) / 2
y = (1 + 0.6 * np.sin(2 * np.pi * x / 0.7) + 0.3 * np.sin(2 * np.pi * x)) / 2

# Step 2: Define Gaussian RBF
def gaussian_rbf(x, c, r):
    """
    Gaussian Radial Basis Function (RBF)
    Parameters:
        x (numpy array): input values
        c (float): center of the RBF
        r (float): radius of the RBF
    Returns:
        numpy array: output of the RBF
    """
    return np.exp(-((x - c) ** 2) / (2 * r ** 2))

# Manually and randomly seleceted hyperparameters
'''
My initial parameters was: 
c1, r1 = 0.3, 0.2 
c2, r2 = 0.8, 0.2
It was pretty off so I changed it to what we have right now.
'''
c1, r1 = 0.2, 0.2  # Parameters for RBF 1
c2, r2 = 0.2, 0.3  # Parameters for RBF 2

# Compute RBF outputs
phi1 = gaussian_rbf(x, c1, r1)
phi2 = gaussian_rbf(x, c2, r2)

# Step 3: Construct design matrix
'''
Output 
'''
Phi = np.vstack([phi1, phi2, np.ones_like(x)]).T
print(Phi)
# Step 4: Train the network (Perceptron Training)
# Using the least squares solution for weight estimation
weights = np.linalg.pinv(Phi).dot(y)

# Extract weights
w1, w2, w0 = weights

# Step 5: Evaluate the network
y_pred = Phi.dot(weights)

# Print weights
print("Weights:")
print(f"w1: {w1}")
print(f"w2: {w2}")
print(f"w0: {w0}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo-', label="Desired Output")
plt.plot(x, y_pred, 'r--', label="RBF Network Output")
plt.title("RBF Network Approximation")
plt.xlabel("Input (x)")
plt.ylabel("Output (y)")
plt.legend()
plt.grid(True)
plt.show()