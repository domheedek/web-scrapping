from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

webdriver_path = '/Users/PC_COM1/chromedriver'

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(webdriver_path, options=options)
url = 'http://www.nice.org.uk/Search.do?searchText=bevacizumab&newsearch=true#/search/?searchText=bevacizumab&mode=&staticTitle=false&SEARCHTYPE_all2=true&SEARCHTYPE_all1=&SEARCHTYPE=GUIDANCE&TOPICLVL0_all2=true&TOPICLVL0_all1=&HIDEFILTER=TOPICLVL1&HIDEFILTER=TOPICLVL2&TREATMENTS_all2=true&TREATMENTS_all1=&GUIDANCETYPE_all2=true&GUIDANCETYPE_all1=&STATUS_all2=true&STATUS_all1=&HIDEFILTER=EGAPREFERENCE&HIDEFILTER=TOPICLVL3&DATEFILTER_ALL=ALL&DATEFILTER_PREV=ALL&custom_date_from=&custom_date_to=11-06-2014&PAGINATIONURL=%2FSearch.do%3FsearchText%40%40bevacizumab%26newsearch%40%40true%26page%40%40&SORTORDER=BESTMATCH'
driver.get(url)
print(len(driver.find_elements_by_css_selector('a.ui-paging-next')))

page_number = 1

while True:
    try:
        link = driver.find_element_by_link_text(str(page_number))
    except NoSuchElementException:
        break
    link.click()
    print(driver.current_url)
    page_number += 1