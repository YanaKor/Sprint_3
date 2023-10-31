import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from base.locators import BASE_URL


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument('chrome')
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')
    # driver.get(BASE_URL)
    yield driver
    driver.quit()
