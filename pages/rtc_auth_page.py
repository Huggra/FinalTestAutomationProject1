from FinalTestAutomationProject.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RostelecomLocators:
    LOCATOR_ROSTELECOM_LOGIN_FIELD = (By.ID, "username")
    LOCATOR_ROSTELECOM_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_ROSTELECOM_LOGIN_BUTTON = (By.ID, "kc-login")
    LOCATOR_ROSTELECOM_FORGOT_BUTTON = (By.ID, "forgot_password")
    LOCATOR_ROSTELECOM_REGISTRATION_BUTTON = (By.ID, "kc-register")
    LOCATOR_ROSTELECOM_ERROR_MESSAGE = (By.ID, "form-error-message")


class RostelecomHelper(BasePage):
    def enter_login_word(self, word):
        search_login_field = self.find_element(RostelecomLocators.LOCATOR_ROSTELECOM_LOGIN_FIELD)
        search_login_field.click()
        search_login_field.send_keys(word)
        return search_login_field

    def enter_password(self, password):
        search_pass_field = self.find_element(RostelecomLocators.LOCATOR_ROSTELECOM_PASSWORD_FIELD)
        search_pass_field.click()
        search_pass_field.send_keys(password)
        return search_pass_field

    def click_login_button(self):
        return self.find_element(RostelecomLocators.LOCATOR_ROSTELECOM_LOGIN_BUTTON).click()

    def click_forgot_button(self):
        return self.find_element(RostelecomLocators.LOCATOR_ROSTELECOM_FORGOT_BUTTON).click()

    def click_registration_button(self):
        return self.find_element(RostelecomLocators.LOCATOR_ROSTELECOM_REGISTRATION_BUTTON).click()

    def check_error_message(self):
        return self.find_element(RostelecomLocators.LOCATOR_ROSTELECOM_ERROR_MESSAGE).text