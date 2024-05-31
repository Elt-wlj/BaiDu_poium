import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture()
def base_url():
    url = r"https://www.baidu.com"
    return url
