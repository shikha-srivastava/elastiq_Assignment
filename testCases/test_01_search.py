import pytest
from PageObject.Search import Search


@pytest.mark.usefixtures('driver')
class Test_search:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.search = Search(self.driver)

    # Test cases to run the test
    @pytest.mark.search
    def test_Search(self):
        self.search.Search_Test()
