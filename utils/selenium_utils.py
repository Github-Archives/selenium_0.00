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

# * Search for your elements in this order-of-presidents: (For speed, simplicity, and readability)

# *id

# *name

# *CSS Selectors


def get_all_h2_tags(driver, timeout=10):
    """Find and return all H2 tags on the page."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2"))
    )


# *XPATH (Good for complex queries, or when I don't have other options, but it's slower and more prone to errors)


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


def time_sleep(seconds):
    """Pause the script for a specified number of seconds."""
    time.sleep(seconds)


def print_here(what_to_print="\tPrinting..."):
    print(f"-> {what_to_print}")


# Midi Ready Project Interactions
def click_note_button(driver, note, timeout=10):
    """Click a button with a specific data-note attribute."""
    selector = f'button[data-note="{note}"]'
    button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    button.click()


def click_notes_sequence(driver, notes, delay=1.5):
    """Click a sequence of note buttons with a delay between each."""
    for note in notes:
        click_note_button(driver, note)
        time.sleep(delay)


def play_midi_music(driver):
    # Click F4, wait 1 second, then click A4
    # (driver, notes, delay=1.5)
    click_notes_sequence(driver, ['F4', 'A4'], delay=1)

    click_notes_sequence(
        driver, ['D4', 'C4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4'], delay=0.33)

    time_sleep(.66)

    click_notes_sequence(
        driver, ['D4', 'F4', 'F4', 'C4'], delay=1.5)
