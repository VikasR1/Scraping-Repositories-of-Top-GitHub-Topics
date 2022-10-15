# little modified code, printing items with single for loop
# getting the details of first page with saved page
import requests
import urllib.request
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import pandas as pd


with open('salon1.html', 'rb') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

name_h3_tag = soup.find_all('h3', class_='css-1agk4wl')

items = len(name_h3_tag)
print("Total elements on the for scrap are {}.".format(items))

items_range = range(len(name_h3_tag))

salons_name = []
yelp_salons_link = []

for i in items_range:
    # get the salon name
    salon_name =name_h3_tag[i].find('a').text
    salons_name.append(salon_name)
    # get the salon url
    link = name_h3_tag[i].find('a')['href']
    base_url = 'https://www.yelp.co.uk'
    full_link = base_url + link
    yelp_salons_link.append(full_link)

scrape_name_link = {
    'Name':salons_name,
    'Url':yelp_salons_link
}
df = pd.DataFrame(scrape_name_link)

print("Printing the items of first page......")
sleep(randint(2,10))
print(df)

    