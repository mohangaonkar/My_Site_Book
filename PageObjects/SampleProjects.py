from selenium.webdriver.common.by import By

class SampleBungalowProject:
    click_sample_bungalow = (By.XPATH, "//span[normalize-space()='Sample bungalow project']")
    click_detailed_estimate = (By.XPATH, "//p[@class='m-0 quote-title-web'][normalize-space()='Detailed Estimate']")

    def __init__(self,driver):
        self.driver=driver

    def bungalowProject(self):
        self.driver.find_element(*self.click_sample_bungalow).click()

    def detailedEstimates(self):
        self.driver.find_element(*self.click_detailed_estimate).click()

