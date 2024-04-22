from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

SEARCH_QUERY = {
    "position": "Test Automation Engineer",
    "location": "United Kingdom", # will include Germany & Netherlands later
}

def login(driver):
    try:
        driver.get("https://www.linkedin.com")
        WebDriverWait(driver, 20).until(EC.url_contains("feed"))
        print("Login successful")
        return True
    except TimeoutException: 
        print("Login failed: Timeout")
        return False

def search_jobs(driver):
    # try:
    WebDriverWait(driver, 30).until(EC.url_contains("/jobs"))
    position_field = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class='jobs-search-box__text-input jobs-search-box__keyboard-text-input']"))
    )
    location_field = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class='jobs-search-box__text-input']"))
    )
    
    # Fill in location and position field with predefined data
    position_field.send_keys(SEARCH_QUERY['position'])
    location_field.send_keys(SEARCH_QUERY['location'])
    time.sleep(1)
    location_field.send_keys(Keys.ENTER)
    
    # driver.find_element(By.XPATH, "//html").click()




    
    """ except TimeoutException:
        print("Search jobs failed: Timeout")
        return False """

if login(driver):
    search_jobs(driver)
    time.sleep(300)
    driver.quit()
