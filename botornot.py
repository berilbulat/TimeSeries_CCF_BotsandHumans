import botometer
import tweepy
import pandas as pd

rapidapi_key = "XXXXX"  
twitter_app_auth = {
    'consumer_key': 'XXXXX',
    'consumer_secret': 'XXXXX',
    'access_token': 'XXXXX',
    'access_token_secret': 'XXXXX',
  }

auth = tweepy.OAuthHandler(twitter_app_auth['consumer_key'], twitter_app_auth['consumer_secret'])
auth.set_access_token(twitter_app_auth['access_token'], twitter_app_auth['access_token_secret'])

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

api = tweepy.API(auth)


tweetChunks = pd.read_csv("xxxx.csv", sep = ' ', iterator=True, chunksize = 100)

for tweetChunk in tweetChunks:
    for tweet in tweetChunk['id_str']:
        print(tweet)
        tweet_info = api.get_status(tweet)
        result = bom.check_account(tweet_info.user.id)
        print(result)
