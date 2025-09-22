import pytest
from selenium import webdriver
from ShopPage import Shop


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    shop_page = Shop(driver)
    shop_page.open()
    shop_page.shop()
    total_text = shop_page.total()
    print(total_text)
    assert total_text == "Total: $58.29"
    shop_page.close_driver()
