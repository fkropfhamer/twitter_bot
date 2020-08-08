import tweepy
import json
import os
from emojis import get_random_emoji
import numpy as np
from PIL import Image
from gan import generate_mnist


def get_secrets():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../config.json')
    with open(filename) as file:
        return json.load(file)


def authenticate():
    secrets = get_secrets()
    
    auth = tweepy.OAuthHandler(secrets['api_key'], secrets['api_key_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

    api = tweepy.API(auth)

    return api


def post_random_emoji(api):
    api.update_status(get_random_emoji())
    

def save_numpy_array_to_png(array, mode='RGB', size=None):
    """
    expects numpy array of shape (height, width, 3) and dtype = np.uint8
    size should be minimum 128x128
    recommended 440x220 or 16:9
    """     

    im = Image.fromarray(array, mode=mode)

    if size:
        im = im.resize(size)

    im.save('numpy_img.png', format="PNG")


def post_image(api, file, message):
    api.media_upload('temp.png')


def upload_numpy_image(api):
    return api.media_upload('numpy_img.png')


def post_image_from_nump_array(api, array, message, mode='RGB', size=None):
    save_numpy_array_to_png(array, mode=mode, size=size)

    media = upload_numpy_image(api)

    api.update_status(message, media_ids=[media.media_id])


def post_randomly_generated_image(api):
    array = np.random.randint(255, size=(900, 1600, 3), dtype=np.uint8)

    post_image_from_nump_array(api, array, get_random_emoji())

def post_mnist_generated_image(api):
    generated_array = generate_mnist()
    post_image_from_nump_array(api, generated_array, get_random_emoji(), mode='L', size=(128,128))
