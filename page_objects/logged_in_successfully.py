from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page_login import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://www.saucedemo.com/inventory.html"
    __menu_button_locator = (By.ID, "menu_button_container")

    def __init__(self, driver: WebDriver):  # to initialize the object, create instance
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    def is_menu_button_displayed(self) -> bool:
        return super()._is_displayed(self.__menu_button_locator)