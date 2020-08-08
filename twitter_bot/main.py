import random
from api import authenticate, post_random_emoji, post_randomly_generated_image, post_mnist_generated_image


def post_random(api):
    choices = [post_random_emoji, post_randomly_generated_image, post_mnist_generated_image]

    choice = random.choice(choices)

    choice(api)

def main():
    api = authenticate()
    
    
    # post_random_emoji(api)
    # post_randomly_generated_image(api)
    # post_mnist_generated_image(api)
    
    post_random(api)


if __name__ == "__main__":
    main()
