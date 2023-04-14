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
driver: WebDriver = webdriver.Chrome(service=service)

driver.get("https://www.techwithtim.net/")

# wait for 10 seconds before closing the browser
print(driver.title)

search = driver.find_element("name", "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# main = driver.find_element("id", "main")
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = driver.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-summary")
        print(header.text)
except:
    driver.quit()

driver.quit()  # close the browser
