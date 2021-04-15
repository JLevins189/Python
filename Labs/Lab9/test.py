
import time
from selenium import webdriver

#link
link = 'http://demo.guru99.com/test/login.html'
#VideoLink = str(input("enter Vid Url"))


driver = webdriver.Chrome()
driver.get(link)
#time.sleep(2)
search_box = driver.find_elements_by_name("email")
search_box.sendKeys("jack")
search_box.submit()




#https://www.youtube.com/watch?v=GbCRLqgUB-o
