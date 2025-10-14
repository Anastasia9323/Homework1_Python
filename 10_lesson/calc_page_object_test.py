import pytest
from selenium import webdriver
from CalculatorPage import Calculator
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    """
    Тест проверяет работу калькулятора.
    :param driver: WebDriver - объект драйвера, переданный фикстурой.
    """
    calculator_page = Calculator(driver)

    with allure.step("Открытие страницы калькулятора"):
        calculator_page.open()

    with allure.step("Изменение времени ожидания"):
        calculator_page.waiting_time()

    with allure.step("Нажатие кнопок"):
        calculator_page.calculation()

    with allure.step("Получение результата с экрана калькулятора"):
        assert calculator_page.result(), "Ожидаемый результат: 15"   

    with allure.step("Завершение работы браузера"):
        calculator_page.close_driver()
