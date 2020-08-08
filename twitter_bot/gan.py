import tflite_runtime.interpreter as tflite
import numpy as np
import os

def generate_mnist():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../models/mnist_model.tflite')
    generator = load_generator(filename)

   
    generated_image = generate(generator)

    generated_image = generate(generator)
    generated_image = normalize(generated_image)

    return generated_image


def generate(interpreter):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test the model on random input data.
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])

    return output_data


def load_generator(path):
    interpreter = tflite.Interpreter(model_path=path)
    interpreter.allocate_tensors()

    return interpreter



def normalize(generated_image):
    generated_image = np.array(generated_image[0, :, :, 0])

    generated_image = generated_image * 127.5 + 127.5

    return generated_image


if __name__ == "__main__":
    m = generate_mnist()
    print(m)
    print(m.shape)
