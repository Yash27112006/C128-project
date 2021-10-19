from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import requests 

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
#print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find_all('table')
print(star_table)

temp_list = []
table_rows = star_table[7].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.replace("\n","") for i in td]
    temp_list.append(row)

print(temp_list)
star_name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=["Star_Name", "Distance", "Mass", "Radius"])
df.to_csv("star.csv")