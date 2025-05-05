import pytest

from page_objects.login_page import LoginPage


# Page Object
class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username,  password, expected_error_message",
                             [("incorrect-user", "secret_sauce", "Epic sadface: Username and password do not match "
                                                                 "any user in this service")])
    def test_negative_username(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"
