from page_objects.web_pages.login_page import LoginPage
from page_objects.web_pages.signup_form import SignUpForm
from page_objects.web_pages.home_page import HomePage

login_page = None
signup_form = None
home_page = None


class ManagePages:

    @staticmethod
    def init_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)
        globals()['signup_form'] = SignUpForm(driver)
        globals()['home_page'] = HomePage(driver)
