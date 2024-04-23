import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_object.exception_page import ExceptionPage


class TestException:
    @pytest.mark.exception
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 should be displayed but its not"

    @pytest.mark.exception
    # @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.add_second_food("sushi")
        assert exceptions_page.get_confirmation_method() == "Row 2 was saved", "Confirmation message is not expected"

    @pytest.mark.exception
    #ytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionPage(driver)
        exceptions_page.open()
        exceptions_page.modify_row1_input("Sushi")
        assert exceptions_page.get_confirmation_method() == "Row 1 was saved","Confirmation message is not expected"


    @pytest.mark.exception
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.are_instruction_displayed(),"Instruction text element should not be displayed"


    #pytest.mark.debug
    @pytest.mark.exception
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 should be displayed but its not"
