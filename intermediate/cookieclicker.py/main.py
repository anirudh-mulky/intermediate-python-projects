from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

button = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
button.click()

timeout = time.time() + 30
while True:
    button = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
    button.click()
    if time.time() > timeout:
        break
