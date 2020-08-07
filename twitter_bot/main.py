import tweepy
import json
import os

def get_secrets():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../config.json')
    with open(filename) as file:
        return json.load(file)

def main():
    secrets = get_secrets()
    
    auth = tweepy.OAuthHandler(secrets['api_key'], secrets['api_key_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

    api = tweepy.API(auth)

    api.update_status("<§")

if __name__ == "__main__":
    main()
