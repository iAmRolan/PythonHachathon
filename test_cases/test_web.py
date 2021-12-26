import pytest

from work_flows.web_work_flows import WebWorkFlows


@pytest.mark.usefixtures('init_web')
class Test_Cases_Web:

    def test_create_user(self):
        self.driver.get("http://localhost:3000/")
        WebWorkFlows.login()


