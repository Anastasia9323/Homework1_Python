import pytest
from selenium import webdriver
from ShopPage import Shop
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование покупки")
@allure.description("Тест проверяет корректность оформления покупки")
@allure.feature("Покупка")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест проверяет корректность оформления покупки.
    :param driver: WebDriver - объект драйвера, переданный фикстурой.
    """
    shop_page = Shop(driver)

    with allure.step("Открытие сайта"):
        shop_page.open()

    with allure.step("Авторизация"):
        shop_page.shop()

    with allure.step("Получение итоговой стоимости"):
        total_text = shop_page.total()
        print(total_text)
        assert total_text == "Total: $58.29"
 
    with allure.step("Завершение работы браузера"):
        shop_page.close_driver()
