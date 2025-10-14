from selenium.webdriver.common.by import By
import allure


class Shop:
    def __init__(self, driver):
        """
        Конструктор класса Shop.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие сайта")
    def open(self):
        """
        Открывает сайт
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация")
    def shop(self):
        """
        Заполняет поля логин и пароль.
        Нажимает на кнопку Login.
        Добавляет товары в корзину.
        Заполняет форму данными.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Анастасия")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Клименкова")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("1234567")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Получение итоговой стоимости")
    def total(self):
        """
        Выводит итоговую стоимость со страницы.
        Сравнивает итоговую сумму с $58.29
        """
        return self.driver.find_element(By.CSS_SELECTOR,
                                        ".summary_total_label").text

    @allure.step("Завершение работы браузера")
    def close_driver(self):
        """
        Закрывает браузер.
        """
        self.driver.quit()
