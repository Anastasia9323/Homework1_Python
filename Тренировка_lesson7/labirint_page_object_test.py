import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages.MainPage import MainPage

def test_cart_counter():
	browser = webdriver.Chrome()  # Открываем браузер
	main_page = MainPage(browser)  # Экземпляр класса с передачей драйвера
	main_page.set_cookie_policy()  # Вызываем метод
