# import libraries
import urllib2
from bs4 import BeautifulSoup

quote_page = "http://www.bloomberg.com/quote/SPX:IND"

page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page,'html.parser')

names = soup.find('h1', attrs={'class': 'name'})

print names
