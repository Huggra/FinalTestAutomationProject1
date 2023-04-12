from selenium.webdriver.common.by import By
from FinalTestAutomationProject.pages.base_page import BasePage

class RostelecomPerAccLocators:
    LOCATOR_ROSTELECOM_PER_ACC = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/h3[1]')

class RostelecomPerAccHelper (BasePage):
    def check_acc_data(self):
        acc_data = self.find_element(RostelecomPerAccLocators.LOCATOR_ROSTELECOM_PER_ACC).text
        return acc_data