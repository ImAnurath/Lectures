import numpy as np
import matplotlib.pyplot as plt
import librosa
from sklearn.metrics import mean_squared_error
import torch
import torch.nn as nn
import torch.optim as optim

# -----------------------
# Load and Normalize Signal
# -----------------------
filename = 'unvoiced_sha.wav'
signal, sr = librosa.load(filename, sr=None)
signal = signal / np.max(np.abs(signal))  # Normalize to [-1, 1]

# -----------------------
# Prepare Input Features and Labels
# -----------------------
order = 20  # Number of past values used for prediction
X = np.array([signal[i:i+order] for i in range(len(signal)-order)])
y = signal[order:]

# -----------------------
# Train/Test Split (70/30)
# -----------------------
split_idx = int(0.7 * len(X))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# Convert to tensors for PyTorch
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.reshape(-1, 1), dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)

# -----------------------
# LINEAR MODEL
# -----------------------
class LinearPerceptron(nn.Module):
    def __init__(self, input_size):
        super(LinearPerceptron, self).__init__()
        self.fc = nn.Linear(input_size, 1)  # No activation function

    def forward(self, x):
        return self.fc(x)

linear_model = LinearPerceptron(order)
criterion = nn.MSELoss()
optimizer = optim.Adam(linear_model.parameters(), lr=0.01)

for epoch in range(400):
    linear_model.train()
    optimizer.zero_grad()
    output = linear_model(X_train_tensor)
    loss = criterion(output, y_train_tensor)
    loss.backward()
    optimizer.step()

linear_model.eval()
with torch.no_grad():
    linear_pred = linear_model(X_test_tensor).numpy().flatten()

# -----------------------
# NONLINEAR MODEL (Feedforward ANN)
# -----------------------
class NonlinearANN(nn.Module):
    def __init__(self, input_size):
        super(NonlinearANN, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 1)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        return self.fc2(x)

nonlinear_model = NonlinearANN(order)
optimizer = optim.Adam(nonlinear_model.parameters(), lr=0.01)

for epoch in range(400):
    nonlinear_model.train()
    optimizer.zero_grad()
    output = nonlinear_model(X_train_tensor)
    loss = criterion(output, y_train_tensor)
    loss.backward()
    optimizer.step()

nonlinear_model.eval()
with torch.no_grad():
    nonlinear_pred = nonlinear_model(X_test_tensor).numpy().flatten()

# -----------------------
# Evaluation (MSE)
# -----------------------
mse_linear = mean_squared_error(y_test, linear_pred)
mse_nonlinear = mean_squared_error(y_test, nonlinear_pred)

print(f"Linear Perceptron MSE: {mse_linear:.6f}")
print(f"Nonlinear ANN MSE: {mse_nonlinear:.6f}")

# -----------------------
# Visualization
# -----------------------
time_axis = np.arange(len(y_test))

plt.figure(figsize=(14, 10))

plt.subplot(3, 1, 1)
plt.plot(time_axis, y_test, label='Original')
plt.plot(time_axis, linear_pred, label='Linear Prediction (Perceptron)')
plt.title('Linear Prediction')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time_axis, y_test, label='Original')
plt.plot(time_axis, nonlinear_pred, label='Nonlinear Prediction (ANN)')
plt.title('Nonlinear Prediction (ANN)')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(time_axis, y_test - linear_pred, label='Linear Error')
plt.plot(time_axis, y_test - nonlinear_pred, label='Nonlinear Error')
plt.title('Prediction Errors (Test Set)')
plt.legend()

plt.tight_layout()
plt.show()
