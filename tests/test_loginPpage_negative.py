import time
import pytest

from selenium.webdriver.common.by import By

from page_object.logged_in_successfully import LoggedInSuccessfullyPage
from page_object.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username,password,expected_error", [
        ("students", "Password123", "Your username is invalid!"), ("student", "Password1234",
                                                                   "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error):
        login_page = LoginPage(driver)
        logged_in_page = LoggedInSuccessfullyPage(driver)
        login_page.open()
        login_page.execute_login(username,password)
        assert login_page.get_error_message() == expected_error, "Error message is not displayed"
