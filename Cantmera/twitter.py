import tweepy

auth = tweepy.OAuthHandler(
    "",
    ""
)
auth.set_access_token(
    "",
    ""
)

# auth = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret, access_token, access_token_secret
# )

api = tweepy.API(auth)

media = api.media_upload("../img/ct4.jpg")

api.update_status(":)", media_ids=[media.media_id_string])

print(api.verify_credentials().screen_name)