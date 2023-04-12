from FinalTestAutomationProject.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RTCRecoveryLocators:
    LOCATOR_ROSTELECOM_RECOVERY = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/h1[1]')

class RTCRecoveryHelper (BasePage):
    def check_recovery_page(self):
        rec_page = self.find_element(RTCRecoveryLocators.LOCATOR_ROSTELECOM_RECOVERY).text
        return rec_page