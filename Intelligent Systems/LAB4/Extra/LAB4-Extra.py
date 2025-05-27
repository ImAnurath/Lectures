import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("test.keras")
path = r'C:\Users\Anurath\Desktop\Projects\Intelligent Systems\LAB4\HandwrittenDigits'

images = []
labels = []
for label in os.listdir(path):
    folder_path = os.path.join(path, label)
    if os.path.isdir(folder_path):
        images.extend([cv2.imread(os.path.join(folder_path, f), cv2.IMREAD_GRAYSCALE) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
        labels.extend([label] * len(os.listdir(folder_path)))

correct_predictions = 0
total_images = len(images)

for i in range(total_images):
    image = images[i]
    image = cv2.resize(image, (28, 28))
    image = np.expand_dims(image, axis=0)
    pred = model.predict(image)
    
    if np.argmax(pred) == int(labels[i]):
        correct_predictions += 1
    
    print(f"Guess: {np.argmax(pred)}\nActual: {labels[i]}")
    plt.imshow(images[i], cmap='gray')
    plt.show()

accuracy = correct_predictions / total_images
print(f"Accuracy: {accuracy * 100:.2f}%")
