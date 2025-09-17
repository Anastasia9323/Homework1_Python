import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_buttons():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)

    # Заполняем обязательные поля
    first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
    first_name.send_keys('Иван')

    last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
    last_name.send_keys('Петров')

    address = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
    address.send_keys('Ленина, 55-3')

    email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
    email.send_keys('test@skypro.com')

    phone_number = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
    phone_number.send_keys('+7985899998787')

    city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
    city.send_keys('Москва')

    # Заполняем дополнительные поля
    country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
    country.send_keys('Россия')
    
    job_position = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
    job_position.send_keys('QA')
    
    company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
    company.send_keys('SkyPro')

    # Нажимаем кнопку Submit
    button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # Ждем обновления страницы
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[name="zip-code"].alert-danger'))
    )

    # Проверяем поле zip-code (должно быть красным)
    zip_code = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
    zip_code_bg_color = zip_code.value_of_css_property("background-color")
    assert "248, 215, 218" in zip_code_bg_color  # Проверяем RGB значения

    # Проверяем остальные поля (должны быть зелеными)
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    
    for field in fields:
        element = driver.find_element(By.CSS_SELECTOR, f'[name="{field}"]')
        bg_color = element.value_of_css_property("background-color")
        assert "209, 231, 221" in bg_color  # Проверяем RGB значения для зеленого

    driver.quit()