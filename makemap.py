#!/usr/bin/python3

import folium 
import pandas 

data = pandas.read_csv("datamap.csv")
map = folium.Map(location = [60, 30.2], zoom_start = 12)

x = data.iloc[:, 2]
y = data.iloc[:, 3]
vote1 = data.iloc[:, 4]
vote2 = data.iloc[:, 5]
vote3 = data.iloc[:, 6]
per1 = data.iloc[:, 8]
per2 = data.iloc[:, 9]
per3 = data.iloc[:, 10]

for x, y, vote1, vote2, vote3, per1, per2, per3 in zip(x, y, vote1, vote2, vote3, per1, per2, per3):
    folium.CircleMarker(location = [x,y], radius = 7, popup = str(vote1) + " (" + str(per1) + "%) For Amosov \n" + str(vote2) + " (" + str(per2) + "%) For Beglov \n" + str(vote3) + " (" + str(per3) + "%) For Tikhonova", icon = folium.Icon(color = 'blue')).add_to(map)

map.save("map.html")
