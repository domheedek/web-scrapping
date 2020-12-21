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
browser = webdriver.Chrome(webdriver_path, options=options)
browser.get(Lazada_url)  # Get Link website you want to scrap

search_bar = browser.find_element_by_id('q')  # ID Searchbar
search_bar.send_keys(search_item)  # Send item you want to Search
search_bar.submit()

# while True:

#     link_page = browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[9]/a')
#     link = []
#     for linkpage in link_page:
#         link.append(linkpage.text)
#     try:
#         browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[9]/a').click()
#     except NoSuchElementException:
#         break

#     print(link)

# #item_stores = browser.find_elements_by_class_name('')
# #item_rating = browser.find_elements_by_class_name('')
item_titles = browser.find_elements_by_class_name('c16H9d')
item_prices = browser.find_elements_by_class_name('c13VH6')

# # Initialize empty lists
titles_list = []
prices_list = []
# stores_list = []
# rating_list = []

# # Loop over the item_titles and item_prices
for title in item_titles:
    titles_list.append(title.text)

for price in item_prices:
    prices_list.append(price.text)

# # for store in item_stores:
# #   stores_list.append(store.text)

# # for rating in item_rating:
# #    rating_list.append(rating.text)

product = dict(zip(titles_list, prices_list))
df = pd.DataFrame.from_dict(product, orient='index')
filterPro = df.filter(like='Pro', axis=0)

print(filterPro)
