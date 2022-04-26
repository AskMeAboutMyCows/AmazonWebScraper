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