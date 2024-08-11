# This will contain your Selenium utility functions.
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ! Original Code For This ↓
# first_link = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[text()='More information...']"))
# )
# first_link.click()
# ! Original Code For This ↑


def click_element(driver, xpath, timeout=10):
    """Wait for an element to be clickable and click it."""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()


def navigate_back(driver, times=1, delay=2):
    """Navigate back a specified number of times with a delay."""
    for _ in range(times):
        driver.back()
        time.sleep(delay)
