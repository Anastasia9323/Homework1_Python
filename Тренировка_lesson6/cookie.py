from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}


driver.get("http://labirint.ru")
driver.add_cookie(my_cookie)

cookie = driver.get_cookie('PHPSESSID')
cookies = driver.get_cookies()

driver.delete_all_cookies()

driver.quit()
