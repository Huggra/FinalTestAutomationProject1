from selenium.webdriver.common.by import By
from FinalTestAutomationProject.pages.base_page import BasePage

class RTCRegistrationLocators:
    LOCATOR_RTC_NAME_FIELD = (By.NAME, "firstName")
    LOCATOR_RTC_LASTNAME_FIELD = (By.NAME, "lastName")
    LOCATOR_RTC_ADDRESS_FIELD = (By.ID, "address")
    LOCATOR_RTC_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_RTC_PASSWORD_CONFIRM_FIELD = (By.ID, "password-confirm")
    LOCATOR_RTC_REGISTRATION_BUTTON = (By.CLASS_NAME, "register-form__reg-btn")
    LOCATOR_RTC_REGISTRATION_PAGE = (By.CLASS_NAME, "card-container__title")
    LOCATOR_RTC_CONFIRM_PAGE = (By.CLASS_NAME, "card-container__title")
    LOCATOR_RTC_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')

class RTCRegistrationHelper(BasePage):
    def enter_firstname(self, firstname):
        firstname_field = self.find_element(RTCRegistrationLocators.LOCATOR_RTC_NAME_FIELD)
        firstname_field.click()
        firstname_field.send_keys(firstname)
        return firstname_field

    def enter_lastname(self, lastname):
        lastname_field = self.find_element(RTCRegistrationLocators.LOCATOR_RTC_LASTNAME_FIELD)
        lastname_field.click()
        lastname_field.send_keys(lastname)
        return lastname_field

    def enter_address(self, address):
        address_field = self.find_element(RTCRegistrationLocators.LOCATOR_RTC_ADDRESS_FIELD)
        address_field.click()
        address_field.send_keys(address)
        return address_field

    def enter_password(self, password):
        password_field = self.find_element(RTCRegistrationLocators.LOCATOR_RTC_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def enter_confirm_password(self, confirm):
        confirm_password_field = self.find_element(RTCRegistrationLocators.LOCATOR_RTC_PASSWORD_CONFIRM_FIELD)
        confirm_password_field.click()
        confirm_password_field.send_keys(confirm)
        return confirm_password_field

    def click_registration_button(self):
        return self.find_element(RTCRegistrationLocators.LOCATOR_RTC_REGISTRATION_BUTTON).click()

    def check_registration_page(self):
        reg_page = self.find_element(RTCRegistrationLocators.LOCATOR_RTC_REGISTRATION_PAGE).text
        return reg_page

    def check_conf_registration_page(self):
        reg_conf_page = self.find_element(RTCRegistrationLocators.LOCATOR_RTC_CONFIRM_PAGE).text
        return reg_conf_page

    def check_error_message(self):
        reg_error_message = self.find_element(RTCRegistrationLocators.LOCATOR_RTC_ERROR_MESSAGE).text
        return reg_error_message