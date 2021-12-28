import os

import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import CommonOps
from utilities.manage_db import ManageDB
from utilities.manage_pages import ManagePages

driver = None
action = None
eyes = None
desired_capabilities = {}

# API
url_api = None
header = None

# xml files paths.
get_data_path = None


@pytest.fixture(scope='class')
def init_web(request):
    browser_type = os.getenv("BrowserType")
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_type.lower == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser_type.lower == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise Exception("Wrong browser type")

    driver.maximize_window()
    globals()['driver'] = driver
    globals()['eyes'] = Eyes()
    globals()['action'] = ActionChains(driver)
    globals()['get_data_path'] = "../files/Web_User_to_test.xml"
    eyes.api_key = CommonOps.get_data("AppliToolsAPIKey")

    request.cls.eyes = eyes
    request.cls.driver = driver
    driver.implicitly_wait(5)

    ManagePages.init_web_pages(driver)

    yield
    # eyes.close()
    driver.quit()
    eyes.abort()


@pytest.fixture(scope='class')
def init_appium(request):
    globals()['get_data_path'] = "../files/mobile_data.xml"
    desired_capabilities['reportDirectory'] = CommonOps.get_data("reportDirectory")
    desired_capabilities['reportFormat'] = CommonOps.get_data("reportFormat")
    desired_capabilities['testName'] = CommonOps.get_data("testName")
    desired_capabilities['uuid'] = CommonOps.get_data("uuid")
    desired_capabilities['appPackage'] = CommonOps.get_data("appPackage")
    desired_capabilities['appActivity'] = CommonOps.get_data("appActivity")
    desired_capabilities['platformName'] = CommonOps.get_data("platformName")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    globals()['driver'] = driver

    request.cls.driver = driver
    driver.implicitly_wait(5)
    ManagePages.init_mobile_pages(driver)

    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_capabilities["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_capabilities["platformName"] = "Windows"
    desired_capabilities["deviceName"] = "WindowsPC"
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_capabilities)
    globals()['driver'] = driver
    globals()['get_data_path'] = "../files/calc_db_query.xml"

    request.cls.driver = driver

    driver.implicitly_wait(5)

    ManagePages.init_desktop_pages(driver)
    ManageDB.setup_db_connection()

    yield
    driver.quit()
    ManageDB.close_connection()


@pytest.fixture(scope="class")
def init_api():
    globals()['get_data_path'] = "../files/api_parameters.xml"
    globals()['url_api'] = CommonOps.get_data("ApiURL")
    globals()['header'] = {'Content-type': 'application/json'}


@pytest.fixture(scope='class')
def init_electron(request):
    globals()['get_data_path'] = "../files/parameters_electron.xml"
    options = webdriver.ChromeOptions()
    options.binary_location = CommonOps.get_data('Electron_App')
    driver = webdriver.Chrome(chrome_options=options, executable_path=CommonOps.get_data('Electron_Driver'))
    globals()['driver'] = driver
    request.cls.driver = driver

    ManagePages.init_electron_pages(driver)

    yield
    driver.quit()
