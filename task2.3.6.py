from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:
    browser.find_element(By.TAG_NAME, 'button').click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    answer = math.log(abs(12 * math.sin(int(x))))
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()