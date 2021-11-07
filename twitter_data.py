import tweepy
import pandas as pd

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True)


message = []
created_at = []
username = []
location = []

for status in tweepy.Cursor(api.home_timeline).items(100):
    message.append(status.text)
    created_at.append(status.created_at)
    username.append(status.user.screen_name)
    location.append(status.user.location)


df = pd.DataFrame({
    "Message":message,
    "Created":created_at,
    "Username":username,
    "Location":location
})

df.to_csv("my_tweet_data.csv")
