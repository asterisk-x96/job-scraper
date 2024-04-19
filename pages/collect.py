from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


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
            return False

def search_jobs(driver):
    try:
        WebDriverWait(driver, 30).until(EC.url_contains("/jobs"))
        position_field = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='jobs-search-box-keyword-id-ember1002']"))
        )
        location_field = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='jobs-search-box-location-id-ember1002']"))
        )
        
        # Fill in location and position field with predefined data
        position_field.send_keys(SEARCH_QUERY['position'])
        ActionChains(driver).move_by_offset(0, 0).click()
        location_field.send_keys(SEARCH_QUERY['location'])

        try:
            driver.find_element_by_xpath("//li/button[text()='United Kingdom']").click()
        except NoSuchElementException:
            pass
        
        return True
    
    except TimeoutException:
        return False

        


login(driver)
search_jobs(driver)
