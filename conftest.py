import pytest
from selenium import webdriver
from pages.account_creating import AccountCreate
from pages.eco_friendly import EcoFriendly
from pages.sale import Sale


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
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
