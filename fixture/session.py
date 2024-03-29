from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        else:
            self.login(username, password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wait = WebDriverWait(wd, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Login']")))

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//a[contains(text(), 'Logout')]")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//td[@class='login-info-left']//span[1]").text == username


