# Pin Counter

## Description
This script allows you to scrape and count the number of pins from a specified Pinterest profile. It uses Selenium for web automation and BeautifulSoup for HTML parsing.

Note: Tested on 15k unsorted pins.

## Usage
1. Ensure you have Python installed on your machine.
2. Install Chrome (Don't use portable version) and download ChromeDriver. They must be the same version, you can download it from[here](https://googlechromelabs.github.io/chrome-for-testing/) (Srcroll down, search for chromedriver of your version) or from [Releases](https://github.com/AlestackOverglow/pin-counter/releases).
3. Install the required packages:
   ```bash
   pip install requests beautifulsoup4 selenium
   ```
4. Open Chrome and log in to Pinterest then you can close it. 
5. Set the profile path to the path of the Chrome profile. You can find it in the Chrome settings. 
   ```python
   # For example:
   profile_path = 'C:/Users/YOUR_USER/AppData/Local/Google/Chrome/User Data'
   ```
6. Set path to the ChromeDriver:
   ```python
   # For example:
   chromedriver_path = 'C:/Users/YOUR_USER/Downloads/chromedriver-win64/chromedriver.exe'
   ```
7. Run the script:
   ```bash
   python pin_counter.py
   ```
8. When prompted, enter the URL of the Pinterest profile you want to scrape. The URL should be in the format:
   `https://{region}.pinterest.com/{username}/_pins/`
9. Script will start after 30 seconds. Wait a while and the script will count the number of pins.
10. Give the repository a star and follow me on GitHub. :P

## License
This project is licensed under the MIT License. 