from page_objects.web_pages.login_page import LoginPage
from page_objects.web_pages.signup_form import SignUpForm
from page_objects.web_pages.home_page import HomePage
from page_objects.web_pages.transactions_page import TransactionsPage
from page_objects.web_pages.bank_account_page import BankAccount
from page_objects.web_pages.notifications_page import Notifications
from page_objects.desktop_pages.calc_main_page import CalcMainPage
from page_objects.mobile_pages.currency_convertor_page import CurrencyConvertorPage
from page_objects.mobile_pages.compound_interest_calc_page import CompoundInterestCalc


# Web
login_page = None
signup_form = None
home_page = None
transactions_page = None
bank_account_page = None
notifications_page = None

# Mobile
currency_convertor_page = None
compound_interest_calc_page = None

# Desktop
calc_main_page = None


class ManagePages:

    @staticmethod
    def init_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)
        globals()['signup_form'] = SignUpForm(driver)
        globals()['home_page'] = HomePage(driver)
        globals()['transactions_page'] = TransactionsPage(driver)
        globals()['bank_account_page'] = BankAccount(driver)
        globals()['notifications_page'] = Notifications(driver)

    @staticmethod
    def init_desktop_pages(driver):
        globals()['calc_main_page'] = CalcMainPage(driver)

    @staticmethod
    def init_mobile_pages(driver):
        globals()['currency_convertor_page'] = CurrencyConvertorPage(driver)
        globals()['compound_interest_calc_page'] = CompoundInterestCalc(driver)
