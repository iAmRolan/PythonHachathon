import pytest
import self as self
from page_objects.web_pages.login_page import LoginPage


login_page = None


class ManagePages:

    @staticmethod
    def init_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)

