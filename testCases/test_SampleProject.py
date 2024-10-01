
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.SampleProjects import SampleBungalowProject
from testCases.test_Login import Test_001_Login
from Utilities.customLogger import LogGen

class Test_002_SampleProject:

    logger=LogGen.loggen()

    @pytest.mark.dependency(depends=["test_login"], name="test_SampleProject")
    def test_bungalowProject(self, setup):
        self.driver = setup
        self.sp = SampleBungalowProject(self.driver)

        self.logger.info("***** Waiting for sample bungalow link *****")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.sp.click_sample_bungalow)
        )

        self.logger.info("***** clicking on sample bungalow project *****")
        self.sp.bungalowProject()

        self.logger.info("***** Waiting for detailed estimate link *****")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.sp.click_detailed_estimate)
        )

        self.logger.info("***** clicking detailed estimate link *****")
        self.sp.detailedEstimates()

        title_estimates = self.driver.title
        self.logger.info(f"***** Title at detailed estimates: {title_estimates} *****")

        try:

            self.logger.info(f"***** Verifying design studio *****")
            element_locator = (By.XPATH, "//label[@class='name']")  # Adjust the XPath or other locator as needed
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator))


            Verifying_design = self.driver.find_element(*element_locator).text
            self.logger.info(f"***** Title at detailed estimates: {Verifying_design} *****")

        except Exception as e:
            self.logger.info(f"An error occurred: {e}")

