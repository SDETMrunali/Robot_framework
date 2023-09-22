from selenium import webdriver
from selenium.webdriver import ActionChains
from robot.libraries.BuiltIn import BuiltIn
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class AutoKeywords:
    @staticmethod
    def get_chromedriver_path():
        driver_path = ChromeDriverManager().install()
        print(driver_path)
        return driver_path
