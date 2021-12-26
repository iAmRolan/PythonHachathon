from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_username_input(self, driver):
        return driver.find_element(By.XPATH, "//input[@id='username']")

