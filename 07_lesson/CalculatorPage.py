from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:
    def __init__(self, driver):
        """
        Конструктор класса Calculator.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
                        "slow-calculator.html")

    @allure.step("Изменение времени ожидания")
    def waiting_time(self):
        """
        Изменяет время ожидания на 45 секунд.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    @allure.step("Нажатие кнопок")
    def calculation(self):
        """
        Нажимает на кнопки калькулятора.
        Ожидает появления результата на экране калькулятора.
        Сравнивает текущий результат с ожидаемым результатом.
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        WebDriverWait(self.driver, 52).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'),
                                             '15'))

    @allure.step("Получение результата с экрана калькулятора")
    def result(self):
        """
        Возвращает текущий результат с экрана калькулятора.
        :return str - текст результата на экране калькулятора.
        """
        res = self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        return res == "15"

    @allure.step("Завершение работы браузера")
    def close_driver(self):
        """
        Закрывает браузер.
        """
        self.driver.quit()
