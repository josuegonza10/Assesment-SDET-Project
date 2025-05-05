import time

import pytest
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


# No page Object
class TestRemoveProduct:
    @pytest.mark.remove
    def test_remove_product(self, driver):
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        # Type username standard_user into Username field
        username_locator = driver.find_element(By.ID, "user-name")
        username_locator.send_keys("standard_user")

        # Type password secret_sauce into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("secret_sauce")

        # Push Submit button
        submit_button_locator = driver.find_element(By.ID, "login-button")
        submit_button_locator.click()

        # add to cart product A "Sauce Labs Backpack"
        submit_product_a = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        submit_product_a.click()

        # add to cart product B "Sauce Labs Fleece Jacket"
        submit_product_b = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        submit_product_b.click()
        time.sleep(5)

        # Navigate to the cart.
        submit_cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        submit_cart_button.click()

        # Verify product A is added
        product_a_added = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
        assert product_a_added.is_displayed(), "Product A is not displayed"

        # Verify product A text is:Sauce Labs Backpack
        message_product_a = product_a_added.text
        assert message_product_a == "Sauce Labs Backpack"
        time.sleep(3)

        # Verify product B is added
        product_b_added = driver.find_element(By.LINK_TEXT, "Sauce Labs Fleece Jacket")
        assert product_b_added.is_displayed(), "Product B is not displayed"

        # Verify product "B" text is:Sauce Labs Fleece Jacket
        message_product_b = product_b_added.text
        assert message_product_b == "Sauce Labs Fleece Jacket"
        time.sleep(3)

        # Remove a product "A" from the cart and validate the change
        remove_product_a = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
        remove_product_a.click()

        # Navigate to the cart.
        submit_cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        submit_cart_button.click()
        time.sleep(3)

        # Verify that product "A" was deleted
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.LINK_TEXT, "Sauce Labs Backpack"))), "Product A should not be displayed"
