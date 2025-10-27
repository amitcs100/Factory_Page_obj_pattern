from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def click(self, by, locator):
        element = self.find(by, locator)
        element.click()

    def enter_text(self, by, locator, value):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(value)

    def is_text_present(self, text):
        return text in self.driver.page_source

    def get_title(self):
        return self.driver.title
