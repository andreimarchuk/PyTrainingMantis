from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognozed browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)

        self.config = config
        self.base_url = config['web']['baseUrl']

    def change_value_by_name(self, name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(text)

    def change_value_by_xpath(self, path, text):
        wd = self.wd
        wd.find_element_by_xpath(path).click()
        wd.find_element_by_xpath(path).clear()
        wd.find_element_by_xpath(path).send_keys(text)

    def select_element_in_dropdown(self, path, value):
        wd = self.wd
        wd.find_element_by_xpath(path).click()
        Select(wd.find_element_by_xpath(path)).select_by_visible_text(value)
        wd.find_element_by_xpath(path).click()


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_to_manage_projects(self):
        wd = self.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

        #if not wd.current_url.endswith("/addressbook/"):
         #   wd.find_element_by_xpath("//a[contains(text(),'home')]").click()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        wd = self.wd
        wd.quit()




