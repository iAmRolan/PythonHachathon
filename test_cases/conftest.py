import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from utilities.manage_pages import ManagePages
from applitools.selenium import Eyes
from utilities.common_ops import CommonOps
from utilities.manage_db import ManageDB



driver = None
action = None
eyes = None
desired_capabilities = {}

# Mobile
reportDirectory = 'reports'
reportFormat = 'xml'
testName = 'Untitled'
uuid = 'ce0517157c63b41702'
appPackage = 'com.financial.calculator'
appActivity = ".FinancialCalculators"
platformName = "android"

# xml files paths.
get_data_path = None


@pytest.fixture(scope='class')
def init_web(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
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
    desired_capabilities['reportDirectory'] = reportDirectory
    desired_capabilities['reportFormat'] = reportFormat
    desired_capabilities['testName'] = testName
    desired_capabilities['uuid'] = uuid
    desired_capabilities['appPackage'] = appPackage
    desired_capabilities['appActivity'] = appActivity
    desired_capabilities['platformName'] = platformName
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    globals()['get_data_path'] = "../files/currency_convertor.xml"
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
