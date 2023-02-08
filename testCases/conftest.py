from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


def pytest_configure(config):
    config._metadata['Project Name'] = 'BDI CR On-site'
    config._metadata['Modul Name'] = 'DCM'
    config._metadata['Tester'] = 'Julianda'


