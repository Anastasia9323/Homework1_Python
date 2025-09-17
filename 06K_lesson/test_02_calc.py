import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    driver = webdriver.Chrome(service=ChromeService
                            (ChromeDriverManager().install()))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    input_field = driver.find_element(By.CSS_SELECTOR, "#delay")

    input_field.clear()

    input_field.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text()='7']").click()

    button_plus = driver.find_element(By.XPATH, "//span[text()='+']").click()

    button_8 = driver.find_element(By.XPATH, "//span[text()='8']").click()

    button_ravno = driver.find_element(By.XPATH, "//span[text()='=']").click()

    waiter = WebDriverWait(driver, 52).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))

    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    print(result)

    assert result == '15'

    driver.quit()