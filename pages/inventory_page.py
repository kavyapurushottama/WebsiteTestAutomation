from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text
