import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, usecols=[1])
plt.plot(data)
plt.title("Air Passenger Data")
plt.ylabel("Passengers")
plt.xlabel("Date/Time")
plt.show()

# Preprocess the data
dataset = data.values
dataset = dataset.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# Split into training and test sets
train_size = int(len(dataset) * 0.70)
train, test = dataset[0:train_size, :], dataset[train_size:, :]

# Create dataset with look-back
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 3
X_train, Y_train = create_dataset(train, look_back)
X_test, Y_test = create_dataset(test, look_back)

# Reshape input for LSTM
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1]))

# Build LSTM model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.LSTM(50, input_shape=(1, look_back)))
model.add(tf.keras.layers.Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, Y_train, epochs=10, batch_size=1, verbose=2)

# Predictions
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Inverse transformation
train_predict = scaler.inverse_transform(train_predict)
Y_train = scaler.inverse_transform([Y_train])
test_predict = scaler.inverse_transform(test_predict)
Y_test = scaler.inverse_transform([Y_test])

# Plot the results
plt.plot(scaler.inverse_transform(dataset), label="True Data")
plt.plot(np.arange(look_back, len(train_predict) + look_back), train_predict, label="Train Prediction")
plt.plot(np.arange(len(train_predict) + (look_back * 2) + 1, len(dataset) - 1), test_predict, label="Test Prediction")
plt.legend()
plt.title("LSTM Time-Series Forecasting")
plt.ylabel("Passengers")
plt.xlabel("Date/Time")
plt.show()

