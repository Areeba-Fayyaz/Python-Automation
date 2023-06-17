#website used : https://tribune.com.pk/story/2420888/govt-bets-on-relief-amnesty

#5- Preparing script to run everyday
#6 -convert py to exe
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

#4 - Headless Mode
from selenium.webdriver.chrome.options import Options
options=Options()
options.headless=True

#1- Creating the driver 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website='https://tribune.com.pk/story/2420888/govt-bets-on-relief-amnesty'
path='I:/chromedriver.exe'

service=Service(executable_path=path)
driver = webdriver.Chrome(service=service)# headless mode 'options'
driver.get(website)



# 2- Finding Element - Extracting Titles and subtitles from the website
containers = driver.find_elements(by="xpath", value="//div[@class='related-post-sdBar']")

#container: //div[@class='related-post-sdBar']
#title: //div[@class='related-post-sdBar']/a/div/p
#subtitle: //div[@class='related-post-sdBar']/a/p[@class='story-date-style no-padding']

for container in containers:
    title = container.find_element(by='xpath', value="./a/div/p").text
    subtitle = container.find_element(by='xpath', value="./a/p[@class='story-date-style no-padding']").text
    #get link of the element
    link=container.find_element(by='xpath', value="./a").get_attribute("href")

# 3- Exporting Data to Csv file
titles=[]
subtitles=[]
links=[]

containers = driver.find_elements(by="xpath", value="//div[@class='related-post-sdBar']")

for container in containers:
    title = container.find_element(by='xpath', value="./a/div/p").text
    subtitle = container.find_element(by='xpath', value="./a/p[@class='story-date-style no-padding']").text
    #get link of the element
    link=container.find_element(by='xpath', value="./a").get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

import pandas as pd
dict={'Titles':titles,'Subtitles':subtitles, 'Links':links}
df_headlines = pd.DataFrame(dict)
filename='Output_Project_2_Preparing_script_to_run_everyday-{month_day_year}.csv'
final_path= os.path.join(application_path, filename)

df_headlines.to_csv(final_path)
driver.quit()




 
