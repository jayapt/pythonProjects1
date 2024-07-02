
# Add a new employee in the PIM module of OrangeHRM


from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest

class Testcase3:
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
    def testaddemp(self, boot):
        try:
           self.driver.get(data.WebData().url)
           self.driver.maximize_window()

           locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
           locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
           assert (self.driver.current_url == self.dashboard)
           print("successfully logged in")

           locator.WebLocators().link_text(self.driver, locator.WebLocators().pimLocator)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().addLocator)
           locator.WebLocators().x_path(self.driver, locator.WebLocators().emp_fn_Locator, data.WebData().emp_firstname)
           locator.WebLocators().x_path(self.driver, locator.WebLocators().emp_ln_locator, data.WebData().emp_lastname)
           locator.WebLocators().x_path(self.driver, locator.WebLocators().emp_id_locator, data.WebData().emp_id)
           locator.WebLocators().clickbutton(self.driver, locator.WebLocators().saveLocator)

           print("successfully added new employee details in PIM module")
        except NoSuchElementException as e:
           print("error")

