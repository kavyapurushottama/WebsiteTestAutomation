from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from testdata.credentials import USERNAME, PASSWORD, URL

def test_add_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open(URL)
    login.login(USERNAME, PASSWORD)

    inventory.add_product_to_cart()
    assert inventory.get_cart_count() == "1"
