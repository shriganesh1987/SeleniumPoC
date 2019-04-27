# pytest sample
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class TestClass:
    def test_browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.google.com')
        driver.close()

    def test_google(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.google.com')
        WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH, "//input[@class='gLFyf gsfi']")))
        driver.close()
