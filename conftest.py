import os
import os.path
from datetime import datetime
import pytest
from selenium import webdriver


# setup and tear down
@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    try:
        yield browser
    finally:
        browser.quit()
