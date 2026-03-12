# LAB4 - Extra
import tensorflow as tf
mnist = tf.keras.datasets.mnist
''' x -> pixel data
    y -> classification
'''
(x_train, y_train),(x_test, y_test) = mnist.load_data()

''' Just Normalization'''
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()

'''
Flatten -> It turns AxB matrix to 1D array. 
In my case (50x70 pixels), I will have a 1D array of 3500 elements
'''
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
'''
These are layers of the Neural Network
Every layer has an activation function.
Number -> 128 means that there are 128 neurons with Relu activation function.

Last layer has 10 neurons with softmax activation function, which is also my output layer.
Reason it got 10, is because I have to classify digits from 0 to 9 hence 10 possible classification.
'''
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation='softmax')) 

'''
Configs for the model.
Optimizer -> Adaptive Moment Estimation -> Adapts the learning rate based on the gradient
Loss -> Apperantly it is great for integer classification and multi-class classification
Metrics -> Accuracy -> Cross checks what NN have decided and what the ground truth is.
'''
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=20)
model.save("MLP.keras")
#AV