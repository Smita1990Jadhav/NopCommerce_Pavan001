

import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser =='chrome':
        driver = webdriver.Chrome()
        #not required to write local path for driver,added driver exe in python libraby root
       # driver=webdriver.Chrome(executable_path="C:\\pythondrivers\chromedriver.exe")

    elif browser=='firefox':
        driver=webdriver.Firefox()
    else:
        driver = webdriver.Edge(executable_path="C:\\pythondrivers\\msedgedriver.exe")
    return  driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
