import pytest


@pytest.mark.usefixtures('init_web')
class Test_Cases_Web:

    def test_create_user(self):
        self.driver.get("http://localhost:3000/")

    