from pages.login_page import LoginPage
from testdata.credentials import USERNAME, PASSWORD, URL

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open(URL)
    login.login(USERNAME, PASSWORD)

    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open(URL)
    login.login("standard_user", "wrong_password")

    error_text = login.get_error_message()
    assert "Username and password do not match" in error_text
