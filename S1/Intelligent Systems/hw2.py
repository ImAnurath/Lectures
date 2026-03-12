import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Generate synthetic time-series data (sine wave)
def generate_data(seq_length=100, num_samples=10000):
    X = []
    y = []
    for _ in range(num_samples):
        start = np.random.randint(0, 1000)
        time_series = np.sin(np.linspace(start, start + seq_length, seq_length))
        X.append(time_series[:-1])  # Input sequence
        y.append(time_series[1:])  # Shifted sequence as target
    return np.array(X), np.array(y)

# Generate data
seq_length = 50
X, y = generate_data(seq_length)

# Reshape data for LSTM: [samples, time steps, features]
X = X.reshape(X.shape[0], X.shape[1], 1)
y = y.reshape(y.shape[0], y.shape[1], 1)

# Create LSTM model
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(50, activation='tanh', return_sequences=True, input_shape=(seq_length-1, 1)),
    tf.keras.layers.Dense(1)  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X, y, epochs=10, batch_size=32, verbose=1)

# Predict on a test sample
test_sample = np.sin(np.linspace(0, seq_length, seq_length))
test_input = test_sample[:-1].reshape(1, seq_length-1, 1)
predicted = model.predict(test_input)

# Plot the result
plt.plot(test_sample[1:], label='True')
plt.plot(predicted.flatten(), label='Predicted')
plt.legend()
plt.title('True vs Predicted')
plt.show()
