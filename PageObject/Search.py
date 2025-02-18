import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utilities.utils import find_element, hover_over_action
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# I have added static time to Just to view the video



class Search:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, driver, by: By, selector: str, timeout: int = 100):
        wait = WebDriverWait(driver, timeout)
        elements = wait.until(EC.visibility_of_element_located((by, selector)))
        return elements

    def Search_Test(self):
        find_element(self.driver, By.CSS_SELECTOR, 'input[type="search"]').send_keys("New York")
        try:
            Entry_text = find_element(self.driver, By.CSS_SELECTOR,'div[role="status"]').text
            search_results, total = Entry_text.split()[4], Entry_text.split()[-3]
            assert search_results == '5', "Search result is not equal to 5"
            assert total =='24', "Total entry is not equal to 24"
        except Exception as e:
            print(f"Search not found due to: {e}")





