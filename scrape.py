import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import date

def get_stock(link):
    driver = webdriver.Chrome()
    #go to the specified link
    driver.get(link)
    #wait for the page to load
    time.sleep(2)
    #pull the html with bs4
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #filter down for the small table under the graph
    soup_data = soup.find_all("td",class_="iyjjgb")
    #collect data
    title = soup.find("span",class_="mfMhoc").text
    open_price = soup_data[0].text
    close_price = soup_data[6].text
    high = soup_data[1].text
    low = soup_data[2].text
    date_stamp = date.today()
    driver.quit()
    return({'company':title, 'open_price':open_price, 'close_price':close_price, 'high':high, 'low':low, 'date':date_stamp})

