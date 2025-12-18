from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from testdata.credentials import USERNAME, PASSWORD, URL

def test_product_visibility(driver):
    login = LoginPage(driver)
    login.open(URL)
    login.login(USERNAME, PASSWORD)

    product = driver.find_element(By.CLASS_NAME, "inventory_item")
    assert product.is_displayed()
