from base.base_object import BaseObject
from base.locators import LogInFormLocators as Login
from support.assertions import Assertions


class LoginPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_login_btn_on_main_page(self):
        self.click(Login.LOGIN_BUTTON_ON_MAIN_PAGE)

    def click_on_personal_account_button(self):
        self.click(Login.PERSONAL_ACCOUNT_BUTTON)

    def open_registration_form(self):
        self.go_to_url('https://stellarburgers.nomoreparties.site/register')

    def click_on_login_btn_on_register_and_recovery_form(self):
        self.click(Login.LOGIN_BUTTON_FROM_REGISTER_AND_RECOVERY_PAGE)

    def open_recovery_form(self):
        self.go_to_url('https://stellarburgers.nomoreparties.site/forgot-password')

    def enter_email_on_login_page(self, email):
        self.type(Login.LOGIN_EMAIL_FIELD, email)

    def enter_password_on_login_page(self, password):
        self.type(Login.LOGIN_PASSWORD_FIELD, password)

    def click_on_login_btn(self):
        self.click(Login.LOGIN_BUTTON)

    def check_text_after_login(self):
        self.assert_equal(self.get_text(Login.HEADER_ON_MAIN_PAGE), 'Соберите бургер')


