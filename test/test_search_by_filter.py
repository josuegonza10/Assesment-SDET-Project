import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as ec


# combined
class TestSearchByFilter:

    @pytest.mark.filter
    def test_filter_by_price(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")
        logged_in_page = LoggedInSuccessfullyPage(driver)

        wait = WebDriverWait(driver, 10)
        dropdown = wait.until(ec.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
        Select(dropdown).select_by_value("lohi")

        wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        products_raw = driver.find_elements(By.CLASS_NAME, "inventory_item")
        products = []

        for product in products_raw:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            price_text = product.find_element(By.CLASS_NAME, "inventory_item_price").text.strip()
            price = float(price_text.replace("$", ""))
            products.append((price, name))

        order = sorted(products)

        if products != order:
            raise AssertionError("The products are not correctly sorted by price and name")
        else:
            print("Successful validation! Products sorted by price and name")


