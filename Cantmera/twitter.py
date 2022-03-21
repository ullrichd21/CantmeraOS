import os

import tweepy
from dotenv import load_dotenv

import graphic


def load_twitter_env():
    load_dotenv("/home/pi/twitter.env")

    api_key = os.getenv('twitter_api_key')
    api_secret = os.getenv('twitter_api_secret')

    access_token = os.getenv('twitter_access_token')
    access_secret = os.getenv('twitter_access_secret')

    # global api
    auth = tweepy.OAuthHandler(
        api_key,
        api_secret
    )
    auth.set_access_token(
        access_token,
        access_secret
    )
    return auth


def tweet_all_photos():
    api = tweepy.API(load_twitter_env())
    photos = os.listdir("/home/pi/photos")
    try:
        for photo in photos:
            tweet(api, os.path.basename(photo))
    except (Exception):
        return False

    for photo in photos:
        os.remove(f"/home/pi/photos/{photo}")

    return True


def tweet(api, photo_name):
    media = api.media_upload(f"/home/pi/photos/{photo_name}")

    api.update_status(f"{photo_name}".replace(".jpg", ""), media_ids=[media.media_id_string])

    print(api.verify_credentials().screen_name)


def get_tweet_screen():
    return graphic.generate_image("Twitter", "Tweeting Photos...",
                                  highlighted=True)
