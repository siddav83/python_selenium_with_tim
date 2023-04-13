
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

PATH = "C:\\Users\\ccaedsi\\Selenium\\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.techwithtim.net/")

time.sleep(10) # wait for 10 seconds before closing the browser
print(driver.title)
driver.quit() # close the browser
