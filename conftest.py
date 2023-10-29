import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument('chrome')
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    url = 'https://stellarburgers.nomoreparties.site/'
    driver.get(url)
    yield driver
    driver.quit()