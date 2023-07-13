import time

from test_data import data


def test_successful_registration(registration_page):
    registration_page.click_on_sign_in_btn()
    registration_page.click_on_register_link()
    registration_page.enter_name(data.name)
    registration_page.enter_email(data.fake_email)
    registration_page.enter_password(data.fake_password)
    registration_page.click_on_register_btn()
    registration_page.check_url_after_registration()


def test_unsuccessful_registration(registration_page):
    registration_page.click_on_sign_in_btn()
    registration_page.click_on_register_link()
    registration_page.enter_name(data.name)
    registration_page.enter_email(data.email)
    registration_page.enter_password('1')
    registration_page.click_on_register_btn()
    registration_page.check_error_message()

