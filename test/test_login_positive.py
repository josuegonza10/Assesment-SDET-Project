import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


# Page Object
class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == login_page.current_url, "Actual URL is not the same"
        assert logged_in_page.is_menu_button_displayed(), "Menu Button should be visible"

        if logged_in_page == login_page:
            raise AssertionError("Login Fail")
        else:
            print("Successful Login")




