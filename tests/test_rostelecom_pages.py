from FinalTestAutomationProject.pages.rtc_auth_page import RostelecomHelper
from FinalTestAutomationProject.pages.rtc_acc_page import RostelecomPerAccHelper
from FinalTestAutomationProject.pages.rtc_recovery_page import RTCRecoveryHelper
from FinalTestAutomationProject.pages.rtc_registration_page import RTCRegistrationHelper


def test_auth_with_phone_TC1(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_per_acc_page = RostelecomPerAccHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("valid phone")
    rtc_main_page.enter_password("valid password")
    rtc_main_page.click_login_button()
    element = rtc_per_acc_page.check_acc_data()
    assert "Учетные данные" in element

def test_auth_with_email_TC2(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_per_acc_page = RostelecomPerAccHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("valid email")
    rtc_main_page.enter_password("valid password")
    rtc_main_page.click_login_button()
    element = rtc_per_acc_page.check_acc_data()
    assert "Учетные данные" in element

def test_auth_with_login_TC3(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_per_acc_page = RostelecomPerAccHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("valid login")
    rtc_main_page.enter_password("valid password")
    rtc_main_page.click_login_button()
    element = rtc_per_acc_page.check_acc_data()
    assert "Учетные данные" in element

def test_auth_with_personal_acc_TC4(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_per_acc_page = RostelecomPerAccHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("valid personal acc")
    rtc_main_page.enter_password("valid password")
    rtc_main_page.click_login_button()
    element = rtc_per_acc_page.check_acc_data()
    assert "Учетные данные" in element

def test_open_recovery_page_TC5(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_rec_page = RTCRecoveryHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_forgot_button()
    element = rtc_rec_page.check_recovery_page()
    assert "Восстановление пароля" in element

def test_open_registration_page_TC6(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    element = rtc_reg_page.check_registration_page()
    assert "Регистрация" in element

def test_auth_with_phone_TC7(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("9210568028")
    rtc_main_page.enter_password("444444")
    rtc_main_page.click_login_button()
    element = rtc_main_page.check_error_message()
    assert "Неверный логин или пароль" in element

def test_auth_with_phone_TC8(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("valid phone")
    rtc_main_page.enter_password("")
    rtc_main_page.click_login_button()
    element = rtc_main_page.check_error_message()
    assert "Неверный логин или пароль" in element

def test_auth_with_phone_TC9(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("invalid phone")
    rtc_main_page.enter_password("invalid password")
    rtc_main_page.click_login_button()
    element = rtc_main_page.check_error_message()
    assert "Неверный логин или пароль" in element

def test_auth_with_phone_TC10(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("")
    rtc_main_page.enter_password("")
    rtc_main_page.click_login_button()
    element = rtc_main_page.check_error_message()
    assert "Неверный логин или пароль" in element

def test_auth_with_phone_TC11(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.enter_login_word("")
    rtc_main_page.enter_password("valid phone")
    rtc_main_page.click_login_button()
    element = rtc_main_page.check_error_message()
    assert "Неверный логин или пароль" in element

def test_registration_new_user_TC12(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("valid name")
    rtc_reg_page.enter_lastname("invalid lastname")
    rtc_reg_page.enter_address("invalid phone")
    rtc_reg_page.enter_password("invalid password")
    rtc_reg_page.enter_confirm_password("invalid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC13(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("valid name")
    rtc_reg_page.enter_lastname("")
    rtc_reg_page.enter_address("")
    rtc_reg_page.enter_password("")
    rtc_reg_page.enter_confirm_password("")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC14(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("invalid name")
    rtc_reg_page.enter_lastname("invalid lastname")
    rtc_reg_page.enter_address("")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC15(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("invalid name")
    rtc_reg_page.enter_lastname("")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("invalid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC16(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("invalid name")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("invalid password")
    rtc_reg_page.enter_confirm_password("")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC17(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("invalid name")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("invalid phone")
    rtc_reg_page.enter_password("")
    rtc_reg_page.enter_confirm_password("invalid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC18(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("")
    rtc_reg_page.enter_lastname("")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC19(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("invalid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("invalid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC20(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC21(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("")
    rtc_reg_page.enter_lastname("invalid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("invalid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC22(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("valid name")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("")
    rtc_reg_page.enter_password("invalid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC23(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("valid name")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("")
    rtc_reg_page.enter_confirm_password("invalid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC24(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("valid name")
    rtc_reg_page.enter_lastname("invalid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_registration_new_user_TC25(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("valid name")
    rtc_reg_page.enter_lastname("")
    rtc_reg_page.enter_address("invalid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" not in element

def test_name_field_TC26(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("А")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_error_message()
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in element

def test_name_field_TC27(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("Аб")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" in element

def test_name_field_TC28(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("Аба")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" in element

def test_name_field_TC29(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("Абабабабабабабабабабабабабаба")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" in element

def test_name_field_TC30(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("Абабабабабабабабабабабабабабаб")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_conf_registration_page()
    assert "Подтверждение телефона" in element

def test_name_field_TC31(browser):
    rtc_main_page = RostelecomHelper(browser)
    rtc_reg_page = RTCRegistrationHelper(browser)
    rtc_main_page.go_to_site()
    rtc_main_page.click_registration_button()
    rtc_reg_page.enter_firstname("Абабабабабабабабабабабабабабаба")
    rtc_reg_page.enter_lastname("valid lastname")
    rtc_reg_page.enter_address("valid phone")
    rtc_reg_page.enter_password("valid password")
    rtc_reg_page.enter_confirm_password("valid conf.pass")
    rtc_reg_page.click_registration_button()
    element = rtc_reg_page.check_error_message()
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in element