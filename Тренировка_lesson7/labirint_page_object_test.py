import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium import webdriver
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_cart_counter():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("Python")

    result_page = ResultPage(browser)
    # result_page.switch_to_table()  # Используем только в видео
    to_be = result_page.add_books()  # Результат вызова add_books

    cart_page = CartPage(browser)
    cart_page.get()  # Переход на страницу с корзиной
    as_is = cart_page.get_counter()  # Текущее значение счетчика на странице 

    assert as_is == to_be


def test_empty_search():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("12345678901234567890")

    result_page = ResultPage(browser)
    msg = result_page.get_first_sentence()

    assert msg == "Пока не нашли для себя ничего в Лабиринте?"
