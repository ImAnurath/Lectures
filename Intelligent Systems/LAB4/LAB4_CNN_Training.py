# LAB4
import os
'''
Just gets rid of the useless terminal warnings
'''
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
mnist = tf.keras.datasets.mnist
''' x -> pixel data
    y -> classification
'''
(x_train, y_train), (x_test, y_test) = mnist.load_data()

'''
Since MNIST dataset's shape is ([Samples], 28, 28) I also changed my x_train and x_test shape to (28, 28, 1)
which afterwards, I made sure that it stays as float and then normalized it.
Since we have convolutional layers, we need to reshape our data to (28, 28, 1) otherwise it wont work properly
'''
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32') / 255
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32') / 255
'''
This is apperently a trick called one-hot encoding.
y labels becomes a list. In my case it is [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] for 0, and [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] for 1
This is also pretty handy for softmax activation function as well as to see other predictions of the system. 

A likely outcome -> [0.2, 0.9, 0.1, 0.4, 0.4, 0.3, 0.7, 1, 0.8, 0] in this scenario, we would get 7 as the prediction
but there are 3 more candidates with 0.7, 0.8 and 0.9 probability
so it helps the visualize the accuracy of the model
'''
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test  = tf.keras.utils.to_categorical(y_test, 10)


model = tf.keras.models.Sequential() # initilize the model

'''
Conv2D -> It is a convolutional layer with relu activation function. We are also specifying the input shape.
(3, 3) -> Kernel Size -> Idea of it is, this is a filter of 3x3 pixels. This is also considered general-purpose for feature extraxtion.
You can always go with 1x1 for speed but it extracts minimal information. Vice versa for 5x5 or 7x7

MaxPooling2D -> Downsampling the feature maps without losing information. It is used to reduce the size of the feature maps.
We use it to reduce the computational complexity, since we are using convolutional layers(Cluttering).
It also helps to reduce overfitting. 
(2,2) is just like kernel size for Conv2D, but it is used to downsample the feature maps. 
'''
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))

'''
Flatten -> It turns AxB matrix to 1D array. Since Dense layer takes 1D array as input
'''
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))  # To reduce overfitting
model.add(tf.keras.layers.Dense(10, activation='softmax'))  # Output layer

# Final step for setting up the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

'''
Batch size is the number of samples processed before the model is updated. 
In the case of CNN it is much more important to update the parameters by using a larger batch size. (MNIST doesnt have too many samples so 64 is fine)
Validation Split -> It is used to split the data into training and validation sets. This is more of a double check to make sure that the model is not overfitting.
'''
history = model.fit(x_train, y_train, epochs=3, batch_size=64, validation_split=0.2)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
model.save("CNN.keras")
#AV