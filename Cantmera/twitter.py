import tweepy

auth = tweepy.OAuthHandler(
    "Bh9K7eFCkp0O9qTEQsNdWprcG",
    "fkgGzc69VxMn1GKueImYXkdXqj3PbNwwjV7FtpwoOOOlrHElXH"
)
auth.set_access_token(
    "1496237541212798980-GGv66g4jLusC4QJbpSNniDGfYXCb9Q",
    "mNjLegekoLwyEPrqvbZBWWCBFMuEJUB7IOLbzZt3fmD7x"
)

# auth = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret, access_token, access_token_secret
# )

api = tweepy.API(auth)

media = api.media_upload("../img/ct4.jpg")

api.update_status(":)", media_ids=[media.media_id_string])

print(api.verify_credentials().screen_name)