#open browser
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.google.pl/')


time.sleep(5)

"""if we want to open browser and doesn't close it
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= options, service=ChromeService(ChromeDriverManager().install())) """

username_locator = driver.find_element(By.XPATH, "//img[@class='lnXdpd']")