
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('https://www.google.pl/')
    #find element by xpath
    myDiv = driver.find_element(By.XPATH, '//div')
    print(myDiv)
    print(myDiv.text)