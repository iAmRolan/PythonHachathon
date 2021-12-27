from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_user_full_name(self):
        return self.driver.find_element(By.XPATH, "//h6[@data-test='sidenav-user-full-name']")

    def get_signup_next_button(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test='user-onboarding-next']")

    def get_signup_bank_acc_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bankaccount-bankName-input']")

    def get_routing_number_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bankaccount-routingNumber-input']")

    def get_account_number_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bankaccount-accountNumber-input']")

    def get_save_button(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test='bankaccount-submit']")

    def get_done_button(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test='user-onboarding-next']")