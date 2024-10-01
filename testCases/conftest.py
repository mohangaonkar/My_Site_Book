import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://mysitebook.io/")
    yield driver
    driver.quit()


