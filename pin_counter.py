import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import sys
import re

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to count pins
def count_pins(driver, profile_url):
    logging.info('Opening profile page...')
    driver.get(profile_url)
    time.sleep(30)  # Wait 30 seconds for page loaded

    # Scroll page for loading all pins
    total_pins_set = set()  # Use set for unique pins
    logging.info('Starting to scroll page for loading pins...')
    no_increase_count = 0  # Counter for no increase
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Increase waiting time
        new_pins = BeautifulSoup(driver.page_source, 'html.parser').find_all('div', {'data-test-id': 'pin'})
        new_pins_set = set(new_pins)  # Use set for unique pins
        previous_count = len(total_pins_set)
        total_pins_set.update(new_pins_set)  # Update the total set of unique pins
        logging.info(f'Found pins: {len(total_pins_set)}')  # Log the number of found pins

        # Check for increase
        if len(total_pins_set) == previous_count:
            no_increase_count += 1
            if no_increase_count >= 3:
                logging.info('The number of pins is not increasing three times in a row. Exiting...')
                break
            time.sleep(5)  # Additional delay
        else:
            no_increase_count = 0  # Reset counter

        time.sleep(2)  # Additional delay for loading new pins

    logging.info(f'Total pins: {len(total_pins_set)}')
    return len(total_pins_set)

def setup_driver(profile_path, chromedriver_path):
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-data-dir={profile_path}')
    options.add_argument("--log-level=3")  # Logging level: 3 - FATAL (only fatal errors)
    return webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Example usage
if __name__ == '__main__':
    profile_url = input('Enter the link to the Pinterest profile: ')

    # Check link format
    if not re.match(r'https://[\w.-]+\.pinterest\.com/[\w.-]+/_pins/', profile_url):
        logging.error('Invalid link format. Link must be in the format https://{YOUR REGION}.pinterest.com/{YOUR USERNAME}/_pins/')
        sys.exit(1)  # Exit the program with an error

    profile_path = 'C:/Users/Alesta/AppData/Local/Google/Chrome/User Data'  # Specify the path to the Chrome profile
    chromedriver_path = 'C:/Users/Alesta/Documents/pinny/chromedriver.exe'  # Specify the path to chromedriver
    driver = setup_driver(profile_path, chromedriver_path)

    try:
        total_pins = count_pins(driver, profile_url)
        print(f'Number of pins: {total_pins}')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:  # Close the driver in any case
        sys.exit()  # Exit the program 