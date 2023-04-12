import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")

    yield driver

    driver.quit()

@pytest.fixture
def browser_size(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)

    yield browser