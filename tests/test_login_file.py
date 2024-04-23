import time
import pytest
from selenium.webdriver.common.by import By

from page_object.logged_in_successfully import LoggedInSuccessfullyPage
from page_object.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        logged_in_page = LoggedInSuccessfullyPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"
