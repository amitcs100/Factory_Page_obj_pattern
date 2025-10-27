import allure
from src.driver_factory import DriverFactory
from src.pages.login_page import LoginPage

@allure.feature("Login Feature")
@allure.story("Login with valid credentials")
def test_login_success():
    # Setup driver and LoginPage with Factory pattern
    driver = DriverFactory.get_driver("chrome")
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    with allure.step("Login to application"):
        login_page.login("standard_user", "secret_sauce")
    with allure.step("Verify login success"):
        assert login_page.is_text_present("Swag Labs")
    DriverFactory.quit_driver(driver)

@allure.feature("Login Feature")
@allure.story("Login with invalid credentials")
def test_login_failure():
    driver = DriverFactory.get_driver("chrome")
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    with allure.step("Attempt login with invalid credentials"):
        login_page.login("standard", "secret_sauce1")
    with allure.step("Verify error message"):
        assert login_page.is_text_present("Epic sadface: Username and password do not match")
    DriverFactory.quit_driver(driver)
