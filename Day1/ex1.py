# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:47:04 2021

@author: pmdun
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
url = "https://proceedings.neurips.cc/"
year = "paper/2020"

#specify number of books
maximum = 10

driver.get(url + year)



#get all book in page
print("Getting all books from page")
bookList = driver.find_element_by_class_name("col").find_elements_by_tag_name("li")

print("Retreving all book's links")
bookLink = []
for i in range(maximum):    
    bookLink.append(bookList[i].find_element_by_tag_name("a").get_attribute("href"))

bookTitle = []
bookAbstract = []

print("Iterating all book")
for link in bookLink:
    driver.get(link)
    title = driver.find_element_by_tag_name("h4").text
    abstract = driver.find_elements_by_tag_name("p")[3].text
    
    print(title)
    print(abstract)

    '''
    bookLink = book.find_element_by_tag_name("a").get_attribute("href")
    element = driver.get(bookLink)
    
    title = element.find_element_by_tag_name("h4").text
    link = url + tail + element.find_elements_by_tag_name("a")[2].get_attribute("href")
    abstract = element.find_elements_by_tag_name("p")[4].text
    
    bookAbstract.append(abstract)
    bookTitle.append(title)
    bookLink.append(link)

print(bookAbstract[0])


bookTitle = [el.find_element_by_tag_name("i").text for el in bookList]

for title in bookTitle:
    print(title)'''