from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys('Ivan')
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('Ivanov')
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('ivan@ivan.ivan')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()
