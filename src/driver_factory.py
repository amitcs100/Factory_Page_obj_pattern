from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            # Use webdriver-manager to handle driver installation automatically
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            return driver
        elif browser == "firefox":
            return webdriver.Firefox()
        elif browser == "edge":
            return webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser type: {browser}")

    @staticmethod
    def quit_driver(driver):
        driver.quit()
