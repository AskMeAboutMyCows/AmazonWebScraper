import csv
from bs4 import BeautifulSoup
#for firefox & chrome
from selenium import webdriver
#for edge
#from msedge.selenium_tools import Edge, EdgeOptions
"""
for chrome
driver = webdriver.Chrome()

for edge
driver = EdgeOptions()
options.use_chromium = true
driver = Edge(options=options)
"""

#for firefox
driver = webdriver.Firefox()

url = "https://www.amazon.com"
driver.get(url)

#this will generate a url from a search term
def get_url(search_term):
    template = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_1"
    search_term = search_term.replace(' ','+')
    return template.format(search_term)
