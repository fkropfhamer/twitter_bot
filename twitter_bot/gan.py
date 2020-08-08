import tensorflow as tf
from tensorflow import keras
import numpy as np

def generate_mnist():
    generator = load_generator('./models/mnist_model.h5')

    generated_image = generate(generator)
    generated_image = normalize(generated_image)

    return generated_image


def generate(generator):
    noise = tf.random.normal([1, 100])
    generated_image = generator(noise, training=False)

    return generated_image


def load_generator(path):
    return keras.models.load_model(path)


def normalize(generated_image):
    generated_image = np.array(generated_image[0, :, :, 0])

    generated_image = generated_image * 127.5 + 127.5

    return generated_image


if __name__ == "__main__":
    m = generate_mnist()
    print(m)
    print(m.shape)
