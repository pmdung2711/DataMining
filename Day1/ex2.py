# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:07:24 2021

@author: pmdun
"""

"""
    class for phone:  vertion2020 large
    id for event: owl-promo
"""



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#initialize chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

#create driver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/Users/pmdun/Downloads/chromedriver_win32/chromedriver.exe")


#specify url
url = "https://www.thegioididong.com/"
driver.get(url)


#get all PHones' url in Page
print("Getting all phones from page")
phones = driver.find_element_by_id("owl-promo").find_elements_by_class_name("owl-item")


print("Retreving all phones' url")
bookLink = []
for i in range(maximum):    
    bookLink.append(bookList[i].find_element_by_class_name("item").find_element_by_tag_name("a").get_attribute("href")
