import pytest
import utilities
from extensions import Verifications
from utilities.manage_pages import ManagePages
from utilities.common_ops import CommonOps
from work_flows.web_work_flows import WebWorkFlows


@pytest.mark.usefixtures('init_web')
class Test_Cases_Web:

    def test_create_user(self):
        self.driver.get("http://localhost:3000/")
        WebWorkFlows.sign_up()
        WebWorkFlows.login_new_user()
        WebWorkFlows.after_first_sign_up()
        Verifications.verify_text(utilities.manage_pages.home_page.get_user_name().text, "@" + CommonOps.get_data("NewUserName"))

    def test_user_balance(self):
        WebWorkFlows.logout()
        WebWorkFlows.login()
        Verifications.verify_text(utilities.manage_pages.home_page.get_user_balance().text, CommonOps.get_data("Balance"))

    def test_transaction(self):
        WebWorkFlows.make_transaction()
        Verifications.verify_text(utilities.manage_pages.transactions_page.get_transaction_amount().text, CommonOps.get_data("ExpectedAmount"))

    def test_create_bank_account(self):
        WebWorkFlows.create_bank_account()
        Verifications.verify_text(utilities.manage_pages.bank_account_page.get_last_bank().text, CommonOps.get_data("NewUserBankAccount"))

    def test_notifications(self):
        WebWorkFlows.navigate_to_notifications()
        self.eyes.open(self.driver, "Test_Notifications_", "Notifying")
        self.eyes.check_window("Notification page")
        WebWorkFlows.delete_notification()
        self.eyes.check_window("After delete")

