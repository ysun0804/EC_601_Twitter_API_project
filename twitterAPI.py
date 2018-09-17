import tweepy
from tweepy import OAuthHandler
import json
import wget

#Twitter API credentials
consumer_key = "wCg7RGNZO9hAh5S0GHYsEZ3qT"
consumer_secret = "j61jEn79uBzjTISSSjaWoaO6e7A1EbuMEoJw8dK7oWGNBqjxvB"
access_token = "1038575555799654400-uNs3cSIYBKx1JL2QPCSISDFiqEMJCw"
access_secret = "nzK8wgBbJd8w3HotuZD4QnLaJ80n5hOrEGBeIYNr8XaJX"
 
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='Mmq30584069',count=200, include_rts=False,exclude_replies=True)

last_id = tweets[-1].id
 
while (True):
    more_tweets = api.user_timeline(screen_name='Mmq30584069',count=200,include_rts=False,exclude_replies=True,max_id=last_id-1)

# There are no more tweets
    if (len(more_tweets) == 0):
      break
    else:
      last_id = more_tweets[-1].id-1
      tweets = tweets + more_tweets

media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
 
for media_file in media_files:
    wget.download(media_file)