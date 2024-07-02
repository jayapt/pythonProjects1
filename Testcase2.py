
# Testcase for Invalid credentials is display

from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest


class Testcase2:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture test
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    # pytest html files
    @pytest.mark.html
    def test_invalidlogin(self, boot):
        try:
            self.driver.get(data.WebData().url)
            self.driver.maximize_window()

            locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
            locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator,data.WebData().wrongpassword)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
            assert (self.driver.current_url != data.WebData().dashboardURL)
            print(f"UNSUCCESSFUL : Logged in with {data.WebData().username} and the password is {data.WebData().wrongpassword}")
            print("Valid username and Wrong password is checked")
        except NoSuchElementException as e:
             print("error")
