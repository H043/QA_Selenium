import pytest
from selenium import webdriver



@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser
