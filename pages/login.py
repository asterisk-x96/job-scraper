from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()

SEARCH_QUERY = {
    "position": "Test Automation Engineer",
    "location": "United Kingdom", # will include Germany & Netherlands later
}

def login(driver):
    driver.get("https://www.linkedin.com")
    while True:
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("feed"))
            print("login successful")
            return True
        except TimeoutException: 
            break
            return False

login(driver)
driver.quit()
