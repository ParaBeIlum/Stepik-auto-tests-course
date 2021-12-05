from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 12 секунд, пока цена не опустится до 100$
    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element(By.TAG_NAME, 'button').click()
    x = browser.find_element(By.ID, "input_value").text
    answer = math.log(abs(12 * math.sin(int(x))))
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()