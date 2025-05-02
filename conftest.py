import pytest
from selenium import webdriver
from pages.account_creating import AccountCreate
from pages.eco_friendly import EcoFriendly
from pages.sale import Sale
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver


@pytest.fixture()
def account_creating(driver):
    return AccountCreate(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale(driver):
    return Sale(driver)
