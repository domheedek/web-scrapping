from selenium import webdriver
from selenium.common.exceptions import *
import re
import pandas as pd

# Enter the file directory of the Chromedriver
webdriver_path = '/Users/PC_COM1/chromedriver'
Lazada_url = 'https://www.lazada.co.th'
search_item = 'iphone 12'  # Choose this because I often search for Pussy!

# Select custom Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

# Open the Chrome browser
browser = webdriver.Chrome(webdriver_path, options = options)
browser.get(Lazada_url)  # Get Link website you want to scrap

search_bar = browser.find_element_by_id('q')  # ID Searchbar
search_bar.send_keys(search_item)  # Send item you want to Search
search_bar.submit()

# Get Link of Product
# link = browser.find_element_by_css_selector('.c16H9d a').get_attribute('href')
link = browser.find_element_by_class_name('c16H9d')
links = link.find_element_by_css_selector('a').get_attribute('href')

print('Link Product is :' + links)
