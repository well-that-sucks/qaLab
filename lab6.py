import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://gmail.com/")
email_address = driver.find_element_by_css_selector("[name=\"identifier\"]")
email_address.send_keys("test_123@mail.ru")
email_address.send_keys(Keys.RETURN)
time.sleep(3)
actual_result = driver.find_element_by_css_selector("[class=\"o6cuMc\"]").text
expected_result = "Не удалось найти аккаунт Google."
assert actual_result == expected_result
email_address.clear()
email_address.send_keys("ztalexgor@gmail.com")
email_address.send_keys(Keys.RETURN)
time.sleep(3)
actual_result = driver.find_element_by_css_selector("[class=\"PrDSKc\"]").text
expected_result = "Возможно, этот браузер или приложение небезопасны. Подробнее…"
assert actual_result == expected_result
driver.close()
