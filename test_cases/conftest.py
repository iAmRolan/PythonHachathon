import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from utilities.manage_pages import ManagePages
from applitools.selenium import Eyes
from utilities.common_ops import CommonOps


driver = None
action = None
eyes = None


@pytest.fixture(scope='class')
def init_web(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    globals()['driver'] = driver
    globals()['eyes'] = Eyes()
    globals()['action'] = ActionChains(driver)
    eyes.api_key = CommonOps.get_data("AppliToolsAPIKey")

    request.cls.eyes = eyes
    request.cls.driver = driver
    driver.implicitly_wait(5)

    ManagePages.init_web_pages(driver)

    yield
    # eyes.close()
    driver.quit()
    eyes.abort()
