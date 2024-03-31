from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    BASE_DIR = Path(__file__).parent.parent
    WEBDRIVER_PATH = BASE_DIR / "chromedriver/chromedriver"
    URL = "https://zoomarket.kz/"
    service = Service(executable_path=WEBDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(URL)
    driver.implicitly_wait(10)
    driver.get(URL)
    request.cls.driver = driver
    yield
    driver.close()
