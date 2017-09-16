# Dependencies
import tweepy
import time
import datetime
import json
import random
import requests as req


# Twitter API Keys
consumer_key = "li1H9TAsg33CyKzoIrFEiv6lu"
consumer_secret = "OIz13cY0E94VRBekXYb1etbgfMzsAZZkfehSIwaizivRrDz2FE"
access_token = "852826422-8lKsBd0AuxXhQcfB23lP4iAp4RSPycf3G4L8YFbJ"
access_token_secret = "VECO7Mh11WijlZG96KBussinNzE5wSukV91xxSZomVbuL"


# In[73]:

happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]


# In[74]:

def city_weather(name):
    api_key = "29afcf3c2590afb091bf6a7b7d7609c4"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = str(name)
    units = "metric"
    # Build partial query URL
    query_url = url + "appid=" + api_key + "&units=" + units + "&q="+city
    print(query_url)
    
    response = req.get(query_url).json()
    return response["main"]["temp"]


# In[75]:

city_weather('London')


# In[76]:

# Create function for tweeting
def HappyItUp():

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
    # Tweet a random quote
    city='London'
    time_str=datetime.datetime.now().strftime("%I:%M %p")
    print(time_str)
    quote_str = " Time:"+time_str+" Weather: "+city+" Temp:"+str(city_weather(city))
    api.update_status(random.choice(happy_quotes)+quote_str)

    # Print success message
    print("Tweeted successfully, sir!")




# In[ ]:

# Set timer to run every minute
while(True):
    HappyItUp()
    time.sleep(60)