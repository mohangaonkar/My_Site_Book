
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    click_yellow_button_login = (By.XPATH, "//a[@class='yellow-btn']")
    text_box_enter_number = (By.XPATH, "//input[@id='mobileNumber']")
    click_button_continue = (By.XPATH, "//button[@type='submit']")
    text_box_enter_password = (By.XPATH, "//input[@id='password']")
    click_button_login = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def ClickHomeLogin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_yellow_button_login)
        ).click()

    def EnterNumber(self, number):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.text_box_enter_number)
        ).send_keys(number)

    def ClickContinue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_button_continue)
        ).click()

    def EnterPassword(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.text_box_enter_password)
        ).send_keys(password)

    def Clicklogin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_button_login)
        ).click()
