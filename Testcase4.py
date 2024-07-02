
# Edit the existing employee in the PIM module

from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest


class Testcase4:
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
    def test_editingemp(self, boot):
        try:
            self.driver.get(data.WebData().url)
            self.driver.maximize_window()
            locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
            locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
            assert (self.driver.current_url == self.dashboard)
            print("successfully logged in")
            locator.WebLocators().link_text(self.driver, locator.WebLocators().pimLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().editLocator)


            emp_firstname = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().employeefirstnamelocator)
            emp_firstname.send_keys(Keys.CONTROL + 'a')
            emp_firstname.send_keys(Keys.DELETE)
            emp_firstname.send_keys(data.WebData().employeefirstname)
            emp_lastname = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().employeelastnamelocator)
            emp_lastname.send_keys(Keys.CONTROL + 'a')
            emp_lastname.send_keys(Keys.DELETE)
            emp_lastname.send_keys(data.WebData().employeelastname)
            emp_id = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().empidlocator)
            emp_id.send_keys(Keys.CONTROL + 'a')
            emp_id.send_keys(Keys.DELETE)
            emp_id.send_keys(data.WebData().empid)
            click_button = self.driver.find_element(by=By.XPATH, value=locator.WebLocators().savebuttonLocator)
            click_button.click()

            print("Successfully edited existing employee information in PIM module")

        except NoSuchElementException as e:
         print("Error")

