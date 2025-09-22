from selenium.webdriver.common.by import By


class Shop:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def shop(self):
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

    def total(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        ".summary_total_label").text

    def close_driver(self):
        self.driver.quit()
