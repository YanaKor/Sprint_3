import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.personal_account import PersonalAccountPage
from pages.logout import LogoutFromAccount
from pages.constructor import Constructor


@pytest.fixture(scope='function')
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture
def setup(get_webdriver):
    url = 'https://stellarburgers.nomoreparties.site/'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()


@pytest.fixture()
def registration_page(setup):
    yield RegistrationPage(setup)


@pytest.fixture()
def login_page(setup):
    yield LoginPage(setup)


@pytest.fixture()
def personal_account(setup):
    yield PersonalAccountPage(setup)


@pytest.fixture()
def logout(setup):
    yield LogoutFromAccount(setup)


@pytest.fixture()
def constructor(setup):
    yield Constructor(setup)
