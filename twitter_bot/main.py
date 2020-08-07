import tweepy
import json
import os
from emojis import get_random_emoji

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

def post_image(api):
    api.update_with_media('code.png', status='?')

def main():
    api = authenticate()
    # post_random_emoji(api)

    
    


if __name__ == "__main__":
    main()
