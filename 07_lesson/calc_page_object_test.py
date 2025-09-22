import pytest
from selenium import webdriver
from CalculatorPage import Calculator


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    calculator_page = Calculator(driver)
    calculator_page.open()
    calculator_page.waiting_time()
    calculator_page.calculation()
    assert calculator_page.result(), "Ожидаемый результат: 15"
    calculator_page.close_driver()
