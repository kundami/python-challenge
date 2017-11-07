
# coding: utf-8

# In[20]:

import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import requests
import pymongo
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from itertools import cycle, islice


# ### Step 1 - Scraping
# 
# #### Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

# In[21]:

def insert_into_mongodb(coll_name,parse_tree):
    conn = 'mongodb://kundami:Malala14@ds243325.mlab.com:43325/heroku_lw7zbvwq'
    client = pymongo.MongoClient(conn)

    # Define database and collection
    try:
        db = client.heroku_lw7zbvwq
        mars_facts = db.mars_facts
        mars_facts.update(
        {},
        parse_tree,
        upsert=True
    )
        return 0
    except:
        return -1


# In[22]:

def scrape_mission_to_mars():
    surf_data = {}
    
    url = "https://mars.nasa.gov/news/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    title = soup.find('title').string
    surf_data['title'] = title
    
    para_list = soup.find_all('p')
    para = []
    for line in para_list:
        para.append(line.string)
    surf_data['paragraphs'] = para  
    
    #Get a List of links 
    links = soup.find_all('a', href=True)
    links_all = []
    links_text = []
    for link in links:
        try:
            #links_text.append(link.string)
            #links_all.append(link.get('href'))
            if link.string is not None:
                surf_data[link.string] = link.get('href')
                coll_name = 'items'
                #insert_into_mongodb(coll_name,post)
                surf_data['paragraphs'] = para.text
                surf_data['title'] = title.text
        except:
            continue
    
    #surf_data['tags'] = links_all
    #surf_data['tags_text'] = links_text
    
        
    #print(para_list)
    return surf_data



# In[ ]:




# In[23]:

#parse_tree = scrape_mission_to_mars()
#print(parse_tree)


# In[24]:

#parse_tree = scrape_mission_to_mars()
#print(parse_tree)
#tags_text = parse_tree['tags_text']
#print(tags_text)




#insert_into_mongodb(parse_tree)


# ###  Function to read the titles and Text and hrefs from mongod

# In[25]:

def read_mongod(coll_name):
    conn = 'mongodb://kundami:Malala14@ds243325.mlab.com:43325/heroku_lw7zbvwq'
    client = pymongo.MongoClient(conn)
    # Define database and collection
    try:
        db = client.heroku_lw7zbvwq
        print(coll_name)
        collection = db[coll_name]
        #collection = db.items
        print(str(db.items.count))
        articles = list(db.collection.find())
        print(articles)
     
        return 0
    except:
        return -1


# In[26]:

#read_mongod('items')


# #### Finding Deatured Image from 
# #### https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

# In[27]:

def scrape_featured_images():
    surf_data = {}
    
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    title = soup.find('title').string
    surf_data['title'] = title
    
    articles = soup.find_all("article")
    for article in articles:
        #print(article.a)
        img_class = article.a['data-fancybox-href']
        img_description = article.a['data-description']
        img_full = url + img_class
        surf_data['featured-image_description'] = img_description
        surf_data['featured-image-url'] = img_full
   
    return surf_data


# In[28]:

#scrape_featured_images()


# #### https://twitter.com/marswxreport?lang=en
# #### Get the Latest Mars weather

# In[29]:

def scrape_twitter():
    surf_data = {}
    
    url = "https://twitter.com/marswxreport?lang=en"
    twit_base_url = "https://twitter.com"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    title = soup.find('title').string
    surf_data['title'] = title
    
    weather_tweets = soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    num=0
    for tweet in weather_tweets:
        #print(str(num))
        if num < 1:
            # print(tweet.prettify())
            latest_weather = tweet.get_text()
            surf_data['latest_weather'] = latest_weather
        num=num+1
        
    return surf_data


# In[30]:

#scrape_twitter()


# In[31]:

def scrape_mars_facts():
    surf_data = {}
    
    url = "https://space-facts.com/mars/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    title = soup.find('title').string
    surf_data['title'] = title
    
    mars_facts = soup.find_all("h2")
    num=0
    rows = soup.findAll('tr')   
    for tr in rows:
        cols = tr.findAll('td')
        if len(cols) > 0:
            fact_type = cols[0].text
            fact_value = cols[1].text
            surf_data[fact_type] = fact_value
        #print(cols)          
    
    return surf_data


# In[32]:

#scrape_mars_facts()


# #### https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
# #### USGS Site scraping to get mars pics

# In[33]:

def scrape_mars_astrogeology():
    surf_data = {}
    
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    base_url='https://astrogeology.usgs.gov'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    
    mars_astros = soup.find_all("a",class_='item product-item')
    num=0
    for astros in mars_astros:
        full_href = base_url+astros['href']
        title = astros.h3.text
        desc = astros.text
        #print(astros.prettify())
        #surf_data[] = desc
        surf_data[title] = full_href
    return surf_data


# In[34]:

#scrape_mars_astrogeology()


# In[36]:

def all_about_mars():
    all_about_mars = scrape_mission_to_mars()
    all_about_mars.update(scrape_featured_images()) 
    all_about_mars.update(scrape_twitter())
    all_about_mars.update(scrape_mars_facts())
    all_about_mars.update(scrape_mars_astrogeology())
    insert_into_mongodb("mars_facts",all_about_mars)
    return all_about_mars




# In[37]:

all_about_mars()


# In[40]:

def read_from_mongodb(coll_name):
    conn = 'mongodb://kundami:Malala14@ds243325.mlab.com:43325/heroku_lw7zbvwq'
    client = pymongo.MongoClient(conn) 
    # Define database and collection
    try:
        db = client.heroku_lw7zbvwq
        mars_facts = db.mars_facts.find_one()
        return mars_facts
    except:
        return {'Mars_facts': "No Facts scraped"}


# In[41]:

read_from_mongodb("mars_facts")


# In[ ]:



