import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page_login import BasePage


class LoginPage(BasePage):
    __url = "https://www.saucedemo.com/"  # __ private
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "login-button")
    __error_message = (By.TAG_NAME, "h3")

    def __init__(self, driver: WebDriver):  # to initialize the object, create instance
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, 3)





