#LAB-1
import random
weight1 = random.uniform(-1, 1)
weight2 = random.uniform(-1, 1)
bias = random.uniform(-1, 1)
learning_rate = 0.1
iteration = 0
max_iteration = 1000

def update_parameters(w1, w2, b, lr, e, x1, x2):
    """
    Updates the parameters of the model by the gradient descent algorithm.
    Parameters:
    w1 (float): The first weight.
    w2 (float): The second weight.
    b (float): The bias.
    lr (float): The learning rate.
    e (float): The error.
    x1 (float): The first feature.
    x2 (float): The second feature.
    """
    w1 = w1 + lr * e * x1
    w2 = w2 + lr * e * x2
    b  = b  + lr * e

    return w1, w2, b
def calculate_error(data):
    error = []
    """
    Calculate the error between the actual output and the predicted output.
    """
    error = []
    for d in data:
        # Calculate the predicted output
        predicted_output = 1 if ((weight1 * d[0]) + (weight2 * d[1]) + bias) > 0 else -1
        # Calculate the error
        error.append(d[2] - predicted_output)
    
    return error

datas = [
    [0.21835,  0.81884,  1],
    [0.14115,  0.83535,  1],
    [0.37022,  0.8111,   1],
    [0.31565,  0.83101,  1],
    [0.36484,  0.8518,   1],
    [0.46111,  0.82518,  1],
    [0.55223,  0.83449,  1],
    [0.16975,  0.84049,  1],
    [0.49187,  0.80889,  1],
    [0.14913,  0.77104, -1],
    [0.18474,  0.6279,  -1],
    [0.08838,  0.62068, -1],
    [0.098166, 0.79092, -1]
]

while iteration < max_iteration:
    errors = calculate_error(datas)
    # Check if all errors are 0. If so, then the algorithm has converged.
    # The all() function returns True if all elements of the iterable are true.
    # In this case, if all errors are 0, then the algorithm has converged.
    if all(e == 0 for e in errors):
        # Print the weights and bias when the algorithm has converged.
        print(f"Converged. Weights: ({weight1}, {weight2}), Bias: {bias}")
        print("Converged.")
        break
    
    for index, data in enumerate(datas):
       weight1, weight2, bias = update_parameters(weight1, weight2, bias, learning_rate, errors[index], data[0], data[1])
       
    iteration += 1
    print(f"Iteration: {iteration}  Weight1: {weight1}, Weight2: {weight2}, Bias: {bias}")
#AV