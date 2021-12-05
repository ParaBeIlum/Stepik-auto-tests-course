from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    answer = str(int(x) + int(y))
    print(answer)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(answer)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()