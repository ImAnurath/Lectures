import numpy as np
import random
class MLP:
    def activation_function(self, x, function_type='sigmoid'):
        if function_type == 'sigmoid':
            return 1 / (1 + np.exp(-x))  # Sigmoid function
        elif function_type == 'tanh':
            return np.tanh(x)
    
    def loss_function(self, predicted, actual):
        return np.mean((predicted - actual) ** 2)
    
    def backpropagation():
        pass
    def init_weights_and_bias(self, neurons):
        in_weights = []
        out_weights = []
        bias = []
        output_bias = random.uniform(-1, 1)
        for n in range(neurons):
            in_weights.append(random.uniform(-1, 1))
            out_weights.append(random.uniform(-1, 1))
            bias.append(random.uniform(-1, 1))
        return in_weights,out_weights,bias, output_bias

def generate_random_input(size, low, high):
    return np.random.uniform(size = size, low = low, high = high)
def generate_random_output(x):
    return (1 + 0.6 * np.sin(2 * np.pi * x/0.7) + 0.3 * np.sin(2 * np.pi * x))/2



inputs = generate_random_input(20, 0, 1)
outputs = generate_random_output(inputs)

print(outputs)