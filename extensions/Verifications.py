import allure


@allure.step("Verify two given strings")
def verify_text(actual_text, expected_text):
    assert actual_text == expected_text
