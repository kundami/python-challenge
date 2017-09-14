# Dependencies
import json
import random
import time
import pandas as pd

import requests as req
from citipy import citipy
import matplotlib.pyplot as plt

# Specify URL
#url = "http://api.openweathermap.org/data/2.5/forecast?"
url = "http://api.openweathermap.org/data/2.5/weather?"
api_key ="29afcf3c2590afb091bf6a7b7d7609c4"
# Make our Request
city="Phoenix"
query_url = url+"appid="+api_key+"&q="+ city
print(query_url)

#Generate cities List

lon_lat_list = []
n = 700
for i in range(0,n):
    coordinate = ( random.randint(-18000.00,18000.00)/100,  random.randint(-9000.00,9000.00)/100 )
    lon_lat_list.append(coordinate)

cities_list = []
cities_dict = {}
for x in lon_lat_list:
    print ( x[0] )
    print( x[1])
    if (citipy.nearest_city(x[1],x[0]) != ""):
        city_name_str = str(citipy.nearest_city(x[1],x[0]).city_name)
        cities_list.append(city_name_str)
        cities_dict.__setitem__(city_name_str, x )

i=0

for city in cities_list:
    print(city)
    i=i+1

print("city count"+str(i))

# Perform API Calls

#create a dataframe from a set of ordered list...
lat = []
lon = []
dt = []
temp =[]
humidity = []
temp_max = []
speed = []
country = []
clouds = []
i=0
try:
    for city in cities_list:
        query_url = url+"appid="+api_key+"&q="+ city
        print(query_url)
        weather_response = req.get(query_url)
        weather_json = weather_response.json()
        lat.append(weather_json["coord"]["lat"])
        lon.append(weather_json["coord"]["lon"])
        dt.append(weather_json["dt"])
        temp.append(weather_json["main"]["temp"])
        humidity.append(weather_json["main"]["humidity"])
        temp_max.append(weather_json["main"]["temp_max"])
        speed.append(weather_json["wind"]["speed"])
        country.append(weather_json["sys"]["country"])
        clouds.append(weather_json["clouds"]["all"])
        i=i+1
        if i == 100:
            i = 0
            time.sleep(5)
except:
    print("Oops!", weather_response.text, "occured.")
    print("City code"+city)
    print()

cities_weather = pd.DataFrame({
                       "cities": cities_list ,
                        "lat" : lat,
                        "lon" :  lon ,
                        "dt" : dt,
                        "temp": temp ,
                        "humidity" : humidity,
                        "temp_max" : temp_max,
                        "speed" : speed ,
                        "country": country,
                        "clouds" : clouds
                       })
cities_weather.to_csv("./output/weather_analysis.csv")
#Build the Graph...
#Latitude vs Temperature Plot
#Create a list of Lat and temp

x_axis = []
y_axis = []
min_x = min(lat)
max_x = max(lat)
min_y = min(temp)-50
max_y= max(temp)+50

# Build a scatter plot for each data type
plt.scatter(lat ,
            temp,
            edgecolor="black", linewidths=1, marker="o",
            alpha=0.8, label="Temp")

# Incorporate the other graph properties
plt.title("Latitude vs temperature")
plt.ylabel("Temperature")
plt.xlabel("Latitude")
plt.grid(True)
plt.xlim([min_x, max_x])
plt.ylim([min_y, max_y])

# Save the figure
#plt.savefig("./output/Population_BankCount.png")

# Show plot
plt.show()


#Build the Graph...
#Latitude vs Humidity next
#Create a list of Lat and temp

min_x = min(lat)
max_x = max(lat)
min_y = min(humidity)-20
max_y= max(humidity)+20

# Build a scatter plot for each data type
plt.scatter(lat ,
            humidity,
            edgecolor="black", linewidths=1, marker="o",
            alpha=0.8, label="Humidity")

# Incorporate the other graph properties
plt.title("Latitude vs Humdity")
plt.ylabel("Humidity")
plt.xlabel("Latitude")
plt.grid(True)
plt.xlim([min_x, max_x])
plt.ylim([min_y, max_y])

# Save the figure
#plt.savefig("./output/Population_BankCount.png")

# Show plot
plt.show()

#Build the Graph...
#Latitude vs Cloudiness next
#Create a list of Lat and temp

min_x = min(lat)
max_x = max(lat)
min_y = min(clouds)-10
max_y= max(clouds)+10


# Build a scatter plot for each data type
plt.scatter(lat ,
            clouds,
            edgecolor="black", linewidths=1, marker="o",
            alpha=0.8, label="Humidity")

# Incorporate the other graph properties
plt.title("Latitude vs Cloudiness")
plt.ylabel("Cloudiness")
plt.xlabel("Latitude")
plt.grid(True)
plt.xlim([min_x, max_x])
plt.ylim([min_y, max_y])

# Save the figure
#plt.savefig("./output/Population_BankCount.png")

# Show plot
plt.show()


#Build the Graph...
#Latitude vs Windspeed next
#Create a list of Lat and temp

min_x = min(lat)
max_x = max(lat)
min_y = min(speed)-20
max_y=  max(speed)+20

# Build a scatter plot for each data type
plt.scatter(lat ,
            speed,
            edgecolor="black", linewidths=1, marker="o",
            alpha=0.8, label="Humidity")

# Incorporate the other graph properties
plt.title("Latitude vs Wind Speed")
plt.ylabel("Wind Speed")
plt.xlabel("Latitude")
plt.grid(True)
plt.xlim([min_x, max_x])
plt.ylim([min_y, max_y])

# Save the figure
#plt.savefig("./output/Population_BankCount.png")

# Show plot
plt.show()

