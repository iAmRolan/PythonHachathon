import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None
action = None


@pytest.fixture(scope='class')
def init_web(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    globals()['driver'] = driver
    request.cls.driver = driver

    yield
    driver.quit()

