# To do

# Authenticate with twitter - Done
# Compile list of RTs to search - Done
# - RT Manchester United tweets every now and then. - Done
# Import Date and Time 
# Figure out a way to write out natural sounding tweets




# Ideas #

# Have it scrap IMDB looking for the latest movies released in the UK to tweet about.



# ------------------------------------------------------------------------------------ #

from key import *
import tweepy
import random
import time


searchterms = ["RT to win",
			"Retweet to win",
			""
]

interests = ["Manchester United",
			"Call of Duty",
			"Game of Thrones",
			"Dunkirk",
			"Kim Kardashian",
			"Big Brother",
			"Real Madrid ",
			"Greggs",
			"Soft Shell Crabs",
			"avocados",
			"Gin",
			]




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



def RTsearch():
	results = api.search('Manchester United', geocode="51.50282,-0.11397")
	for x in results: 
		print x.text
		print '-------'



def RetweetInterest(x):
	# Searchs via geocode - currently set to a 10km radius around Central London
	results = api.search(x,geocode="51.50282,-0.11397,10km")
	for x in results:
		if "RT" and "@" not in x.text:
			print x.text
			print '------'
			print time.strftime("%I:%M")


# def WriteStatusInterest(x):



RetweetInterest(random.choice(interests))

