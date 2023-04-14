from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\\Users\\ccaedsi\\Selenium\\chromedriver.exe"
service = Service(PATH)
# driver: WebDriver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(PATH)
driver.get("https://www.techwithtim.net/")

link = driver.find_element(By.LINK_TEXT, "Game Development With Python")
link.click()

try:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "General Pygame Tutorial"))
    )
    link.click()

    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    link.click()
    driver.back()
    driver.back()
    driver.back()
except:
    driver.quit()
