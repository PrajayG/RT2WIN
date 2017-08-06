# To do

# Authenticate with twitter
# Compile list of RTs to search 
# - RT Manchester United tweets every now and then. 



# ------------------------------------------------------------------------------------ #

import tweepy






auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

# def ManchesterUnited():
# 	API.retweet(id)
def RTsearch():
	results = api.search('RT to win')
	for x in results: 
		print x.text



RTsearch()

