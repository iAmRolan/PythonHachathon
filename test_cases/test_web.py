import time

import pytest
import utilities
from extensions import Verifications
from utilities.manage_pages import ManagePages

from work_flows.web_work_flows import WebWorkFlows


@pytest.mark.usefixtures('init_web')
class Test_Cases_Web:

    def test_create_user(self):
        self.driver.get("http://localhost:3000/")
        WebWorkFlows.sign_up()
        time.sleep(2)
        WebWorkFlows.login()
        time.sleep(2)
        WebWorkFlows.after_first_sign_up()
        Verifications.verify_text(utilities.manage_pages.home_page.get_user_full_name().text, "TestUser3 T")




