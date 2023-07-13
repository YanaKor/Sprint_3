from test_data import data


def test_logout_by_clicking_on_logout_button_in_personal_account(login_page, logout):
    login_page.click_on_personal_account_button()
    login_page.enter_email_on_login_page(data.email)
    login_page.enter_password_on_login_page(data.password)
    login_page.click_on_login_btn()
    login_page.click_on_personal_account_button()
    logout.click_on_logout_button()
    logout.check_text_after_logout()
