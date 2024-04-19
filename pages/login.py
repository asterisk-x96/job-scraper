from selenium import webdriver
from selenium.webdriver.common.by import By

SEARCH_QUERY = {
    "position": "Software QA Engineer",
    "location": "United Kingdom", # will include Germany & Netherlands later
}

def login(driver):
    driver.get("https://www.linkedin.com")
    while True:
        try:
            WebDriverWait(driver, 1).until(EC.contains("feed"))
        except TimeoutException: 
            break
    return True