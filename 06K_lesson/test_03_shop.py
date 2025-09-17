import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def test_shop():
    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    add_product_1 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    add_product_2 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    add_product_3 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    basket = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    checkout_button = driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Анастасия")

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Клименкова")

    zip_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    zip_code.send_keys("1234567")

    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    txt = total.text

    print(txt)

    assert txt == "Total: $58.29"

    driver.quit()