#Creating the driver 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website='https://news.google.com/home?hl=en-PK&gl=PK&ceid=PK:en'
path='I:/chromedriver.exe'

service=Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)


# Extracting Titles and subtitles from the website
containers = driver.find_elements(by="xpath", value="//div[@class='related-post-sdBar']")

#container: //div[@class='related-post-sdBar']
#title: //div[@class='related-post-sdBar']/a/div/p
#subtitle: //div[@class='related-post-sdBar']/a/p[@class='story-date-style no-padding']

for container in containers:
    title = container.find_element(by='xpath', value="./a/div/p").text
    subtitle = container.find_element(by='xpath', value="./a/p[@class='story-date-style no-padding']").text
    #get link of the element
    container.find_element(by='xpath', value="./a").get_attribute("href")
