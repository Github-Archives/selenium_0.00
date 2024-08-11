from selenium import webdriver

from utils import click_element, navigate_back, time_sleep, get_all_h2_tags, print_here

# Initialize WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox(), webdriver.Edge(), etc.

# Open the initial webpage
driver.get("https://www.example.com")
# Click the first link
click_element(driver, "//a[text()='More information...']")

click_element(driver, "//a[text()='IANA-managed Reserved Domains']")
time_sleep(1)  # pauses the script for (n) seconds


click_element(driver, "//a[text()='XN--HGBK6AJ7F53BBA']")
time_sleep(1)

print_here("\n\nThis is a test message.")
time_sleep(1)

# Get all H2 tags
h2_tags = get_all_h2_tags(driver)

# Print the number of H2 tags found
print(f"Number of H2 tags found: {len(h2_tags)}\n")

print("Print each H2 tags text")
# Print each H2 tag's text
for index, h2 in enumerate(h2_tags, start=1):
    print(f"\nH2 tag #{index}: {h2.text}")

# ? Too much data for now
# print("HTML Content")
# # If you want to see the HTML content of the H2 tags
# for index, h2 in enumerate(h2_tags, start=1):
#     print(
#         f"HTML Content\nH2 tag #{index} HTML: {h2.get_attribute('outerHTML')}")

# Navigate back three times
navigate_back(driver, times=3, delay=2)


# Click the first link again
click_element(driver, "//a[text()='More information...']")
time_sleep(2)

# Close the browser
driver.quit()
