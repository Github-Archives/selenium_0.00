import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox(), webdriver.Edge(), etc.

# Open the initial webpage
driver.get("https://www.example.com")

# Wait for the first link to be clickable and click it
first_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='More information...']"))
)
first_link.click()

# Wait for the second page to load and the second link to be clickable
iana_managed_domains = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[text()='IANA-managed Reserved Domains']"))
)

# Click the second link
iana_managed_domains.click()

# Wait for a few seconds to observe the result
time.sleep(3)  # pauses the script for 2 seconds


# Wait for the second page to load and the second link to be clickable
third_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[text()='XN--HGBK6AJ7F53BBA']"))
)
third_link.click()
time.sleep(3)  # pauses the script for 3 seconds

# Navigate back to the previous page
driver.back()

time.sleep(0.5)

driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

first_link.click()
time.sleep(2)

# Close the browser
driver.quit()
