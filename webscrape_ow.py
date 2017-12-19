import requests
from BeautifulSoup import BeautifulSoup
import numpy as np
import pandas as pd
import json
import csv
from datetime import datetime

#----------VARIABLE DECLARATIONS ----------#
hero_urls = []
json_dict = []

def get_heroes():
    # Begin making the soup from BeautifulSoup and call teh HTML Requests
    url = 'http://overwatch.wikia.com/wiki/Overwatch_Wiki'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)

    urls = soup.find('div',attrs={'id': 'gallery-0'}).findAll('div',attrs={'class':'lightbox-caption'})

    for el in urls:
        a = el.find("a")['href']
        hero_urls.append(a)

# SCRAPE HERO PAGES FOR DATA
def page_scrape(arg):
    #scrape a page
    hero_lib = {}
    print arg
    url = arg
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    # Need to grab the name of the hero and format proper JSON
    stat_titles = soup.findAll('h3',attrs={'class':'pi-data-label pi-secondary-font'})
    stat_values = soup.findAll('div', attrs={'class':'pi-data-value pi-font'})

    l = 0
    while l < len(stat_titles):
        v =  stat_values[l].text
        t =  stat_titles[l].find('b').text
        hero_lib[t] = v
        l = l + 1
    print hero_lib
    json_dict.append(hero_lib)
    # df = pd.DataFrame(hero_lib)
    # print df
    # print 'SCRAPPED!'
    # pr(int "======================="

#--------------------------#
#-------Begin Program------#
#--------------------------#

#Get URLS for all heroes on OverWatch wiki
#Using http://overwatch.wikia.com/wiki/Overwatch_Wiki
get_heroes()

#Take all URLS and iterate through them to generate data set
for el in hero_urls:
    customURL = 'http://overwatch.wikia.com'+ el
    page_scrape(customURL)


#----------------------------#
#---Output Data to file(s)---#
#----------------------------#

#Print to JSON
print json_dict[0]['Difficulty:']
json_string = json.dumps(json_dict)

with open('data.json', 'w') as outfile:
    json.dump(json_string, outfile)
