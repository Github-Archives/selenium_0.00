import time

from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

# ! Old way without utilizing __init__.py to import functions from selenium_utils.py as a package ↓
# from utils.selenium_utils import click_element, navigate_back
from utils import click_element, navigate_back

# Initialize WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox(), webdriver.Edge(), etc.

# Open the initial webpage
driver.get("https://www.example.com")

# Click the first link
click_element(driver, "//a[text()='More information...']")

# Click the second link
click_element(driver, "//a[text()='IANA-managed Reserved Domains']")
time.sleep(3)  # pauses the script for 3 seconds

# Click the third link
click_element(driver, "//a[text()='XN--HGBK6AJ7F53BBA']")
time.sleep(3)  # pauses the script for 3 seconds

# Navigate back three times
navigate_back(driver, times=3, delay=2)

# Click the first link again
click_element(driver, "//a[text()='More information...']")
time.sleep(2)  # pauses the script for 2 seconds

# Close the browser
driver.quit()
