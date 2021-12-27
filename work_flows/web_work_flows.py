import login as login

import utilities
from extensions.UIActions import UIActions
from utilities.manage_pages import ManagePages


class WebWorkFlows:

    @staticmethod
    def login():
        # TODO Send keys from external file.
        UIActions.send_keys_to_element(utilities.manage_pages.login_page.get_username_input(), "TUser3")
        UIActions.send_keys_to_element(utilities.manage_pages.login_page.get_password_input(), "123456")
        UIActions.click_element(utilities.manage_pages.login_page.get_login_button())

    @staticmethod
    def sign_up():
        # TODO Send keys from external file.
        UIActions.click_element(utilities.manage_pages.login_page.get_signup_button())
        UIActions.click_element(utilities.manage_pages.login_page.get_signup_button())
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_first_name_input(), "TestUser3")
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_last_name_input(), "TestUser3LN")
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_username_input(), "TUser3")
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_password_input(), "123456")
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_confirm_password_input(), "123456")
        UIActions.click_element(utilities.manage_pages.signup_form.get_signup_button())

    @staticmethod
    def after_first_sign_up():
        # TODO Send keys from external file.
        UIActions.click_element(utilities.manage_pages.home_page.get_signup_next_button())
        UIActions.send_keys_to_element(utilities.manage_pages.home_page.get_signup_bank_acc_input(), "TestBank")
        UIActions.send_keys_to_element(utilities.manage_pages.home_page.get_routing_number_input(), "123123123")
        UIActions.send_keys_to_element(utilities.manage_pages.home_page.get_account_number_input(), "123456789")
        UIActions.click_element(utilities.manage_pages.home_page.get_save_button())
        UIActions.click_element(utilities.manage_pages.home_page.get_done_button())
