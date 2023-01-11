from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_button_exist(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)

    button = browser.find_element(By.CSS_SELECTOR, "button[class*='basket']")

    assert button, 'Кнопка отсутствует на сайте'