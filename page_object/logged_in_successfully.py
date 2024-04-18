from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/practice-test-login/"
    __header_locator = (By.TAG_NAME, "h1")
    __button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
   

    @property
    def expected_url(self) -> str:
        return self._url

    def get_header(self) -> str:
        super()._get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:
        super().is_logout_button_displayed(self.__button_locator)

