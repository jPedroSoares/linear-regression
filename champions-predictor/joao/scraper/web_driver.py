# web_driver.py

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

def configWebDriver() -> WebDriver:
    """
    Configure and return a WebDriver for Firefox.

    Return:
        WebDriver: a instance of WebDriver configured for Firefox.
    """
    firefox_options = Options()
    firefox_options.add_argument('--headless')  # Execute em headless mode (without GUI)

    driver = Firefox(options=firefox_options)
    return driver
