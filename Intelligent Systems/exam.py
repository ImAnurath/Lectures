import numpy as np
import random

'''
Activation Functions
'''
def tanh(x):  # p1
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def linear(x):  # p2
    return x

def sigmoid(x):  # p3
    return 1 / (1 + np.exp(-x))
def tanh_derivative(x):
    return 1 - tanh(x) ** 2

def linear_derivative(x):
    return 1

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

'''
Inputs
'''
x_input = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Example input sequence

'''
First Layer has 2 nodes with 4 connections, activation function tanh
'''
weights_layer1 = np.array([random.uniform(-1, 1) for _ in range(4)]).reshape(2, 2)  # 2x2 weight matrix
bias_layer1 = np.array([random.uniform(-1, 1) for _ in range(2)])  # 2 biases

'''
Second Layer has 3 nodes with 6 connections, activation function linear
'''
weights_layer2 = np.array([random.uniform(-1, 1) for _ in range(6)]).reshape(3, 2)  # 3x2 weight matrix
bias_layer2 = np.array([random.uniform(-1, 1) for _ in range(3)])  # 3 biases

'''
Third Layer has 1 node with 3 connections, activation function sigmoid
'''
weights_layer3 = np.array([random.uniform(-1, 1) for _ in range(3)]).reshape(1, 3)  # 1x3 weight matrix
bias_layer3 = np.array([random.uniform(-1, 1) for _ in range(1)])  # 1 bias

'''
Recurrent Connection Initialization
'''
previous_output = 0  # Initialize the previous output (y(n-1)) to 0
y_output = []
y_true = np.array([0.2, 0.1, 1, 0.6, 0.9, 0, 0.8, 0.3, 0.4, 0.5])
learning_rate = 0.01
'''
Running the network
'''
for i,x in enumerate(x_input):
    # Combine input x and previous output
    input_layer1 = np.array([x, previous_output])  # Input is x and y(n-1)
    
    # First layer: 2 nodes with tanh activation
    output_layer1 = tanh(np.dot(weights_layer1, input_layer1) + bias_layer1)
    
    # Second layer: 3 nodes with linear activation
    output_layer2 = linear(np.dot(weights_layer2, output_layer1) + bias_layer2)
    
    # Third layer: 1 node with sigmoid activation
    output_layer3 = sigmoid(np.dot(weights_layer3, output_layer2) + bias_layer3)
    
    # Store the final output and update the previous output
    y_output.append(float(output_layer3[0]))
    previous_output = float(output_layer3[0])
    
    # Loss calculation
    loss = (y_true[i] - y_output[i]) ** 2

    # Backpropagation
    # Gradients for third layer
    error3 = 2 * (y_output[i] - y_true[i]) * sigmoid_derivative(output_layer3)
    grad_weights3 = error3 * output_layer2
    grad_bias3 = error3

    # Gradients for second layer
    error2 = np.dot(weights_layer3.T, error3) * linear_derivative(output_layer2)
    grad_weights2 = np.outer(error2, output_layer1)
    grad_bias2 = error2

    # Gradients for first layer
    error1 = np.dot(weights_layer2.T, error2) * tanh_derivative(output_layer1)
    grad_weights1 = np.outer(error1, input_layer1)
    grad_bias1 = error1

    # Update weights and biases
    weights_layer3 -= learning_rate * grad_weights3
    bias_layer3 -= learning_rate * grad_bias3

    weights_layer2 -= learning_rate * grad_weights2
    bias_layer2 -= learning_rate * grad_bias2

    weights_layer1 -= learning_rate * grad_weights1
    bias_layer1 -= learning_rate * grad_bias1
# Print the output for the given input sequence
print("Input Sequence: ", x_input)
print("Output Sequence: ", y_output)
