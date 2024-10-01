
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Login import  LoginPage
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen

class Test_001_Login:


    baseURL=readconfig.appURL()
    usernumber=readconfig.Usernumber()
    password=readconfig.Password()

    logger = LogGen.loggen()

    @pytest.mark.dependency(name="test_login")
    def test_login(self,setup):
        self.logger.info("***** ***** Validating: Test_001_Login ***** *****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.logger.info("***** Opening the base URL *****")

        try:
            self.logger.info("***** Waiting for the popup close button to appear *****")
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//img[@src='https://mysitebook.io/wp-content/themes/mysitebook/assets/images/knowledge/close.svg']"))

            )

            close_button.click()
            self.logger.info("***** Popup closed successfully *****")

        except Exception as e:
            self.logger.error(f"***** Popup close failed:{e} *****")

        self.logger.info("***** Initiating login process *****")
        self.lp = LoginPage(self.driver)

        self.logger.info("***** Clicking Home login button *****")
        self.lp.ClickHomeLogin()

        all_tabs=self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])
        self.logger.info("***** Switched to new tab *****")

        title=self.driver.title
        self.logger.info(f"***** Page title after switching tab:{title} *****")


        self.logger.info("***** Entering usrname *****")
        self.lp.EnterNumber(self.usernumber)

        self.logger.info("***** clicking continue button *****")
        self.lp.ClickContinue()

        self.logger.info("***** Entering password *****")
        self.lp.EnterPassword(self.password)

        self.logger.info("***** clicking on login button *****")
        self.lp.Clicklogin()
        self.logger.info("***** Login Successfull *****")




