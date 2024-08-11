# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# # Set up the Chrome WebDriver using webdriver-manager
# driver = webdriver.Chrome(ChromeDriverManager().install())

# # Open a webpage
# driver.get("https://www.google.com")

# # Perform any actions on the webpage
# print(driver.title)

# # Close the browser
# driver.quit()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# # Set up the Chrome WebDriver using webdriver-manager
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# # Open a webpage
# driver.get("https://www.google.com")

# # Perform any actions on the webpage
# print(driver.title)

# # Close the browser
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox(), webdriver.Edge(), etc.

# Open a webpage
driver.get("https://www.reddit.com")

# Find an element
search_box = driver.find_element("name", "q")

# Interact with the element
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
driver.implicitly_wait(10)  # waits up to 10 seconds

# Close the browser
driver.quit()
