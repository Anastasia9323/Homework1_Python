from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

search_box = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
search_box.send_keys("Selenium", Keys.RETURN)

sleep(5)
driver.quit()
