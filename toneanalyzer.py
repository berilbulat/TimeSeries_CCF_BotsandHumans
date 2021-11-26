from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import json
import pandas as pd
import tweepy

twitter_app_auth = {
    'consumer_key': 'XXXXX',
    'consumer_secret': 'XXXXX',
    'access_token': 'XXXXX',
    'access_token_secret': 'XXXXX',
  }

auth = tweepy.OAuthHandler(twitter_app_auth['consumer_key'], twitter_app_auth['consumer_secret'])
auth.set_access_token(twitter_app_auth['access_token'], twitter_app_auth['access_token_secret'])

api = tweepy.API(auth)

apiKey = "XXXXX"
toneURL = "XXXXX"

try:
    authenticator = IAMAuthenticator(apiKey)
    tone_analyzer = ToneAnalyzerV3(
        version='XXXXX',
        authenticator=authenticator
    )
    tone_analyzer.set_service_url(toneURL)
    tone_analyzer.set_detailed_response(True)

    tweetChunks = pd.read_csv("XXX.csv", sep = ' ', iterator=True, chunksize = 100)

    for tweetChunk in tweetChunks:
        for tweet in tweetChunk['id_str']:
            try:
                print(tweet)
                tweet_info = api.get_status(tweet, tweet_mode="extended")
                print(tweet_info.full_text)
                if tweet_info.full_text:
                    tone_analysis = tone_analyzer.tone( {'text': tweet_info.full_text},content_type='application/json' ).get_result()
                    print(json.dumps(tone_analysis, indent=2))
            except Exception as ex:
                print("Failed with status code: " + str(ex))
                continue

except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)
