from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:
    x = browser.find_element(By.ID, "input_value").text
    answer = math.log(abs(12 * math.sin(int(x))))
    # Scrolling footer
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()