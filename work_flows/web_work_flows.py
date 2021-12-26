from extensions.UIActions import UIActions
from utilities.manage_pages import ManagePages
import utilities


class WebWorkFlows:

    @staticmethod
    def login():
        UIActions.send_keys_to_element(utilities.manage_pages.login_page.get_username_input(), "Rolo")
