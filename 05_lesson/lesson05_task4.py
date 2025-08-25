from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

input_username = driver.find_element(By.CSS_SELECTOR, "#username")
input_username.send_keys("tomsmith")

input_password = driver.find_element(By.CSS_SELECTOR, "#password")
input_password.send_keys("SuperSecretPassword!")

button_click = driver.find_element(By.CSS_SELECTOR, ".radius").click()

print('You logged into a secure area!')

driver.quit()
