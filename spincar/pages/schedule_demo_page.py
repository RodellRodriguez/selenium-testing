from selenium import webdriver

from .base_page import BasePage


class ScheduleDemoPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://info.spincar.com/360-demo-2'

    def navigate(self):
        self.browser.get(self.url)

    def set_first_name(self, first_name):
        element = self.browser.find_element_by_name('firstname')
        element.send_keys(first_name)
    
    def set_last_name(self, last_name):
        element = self.browser.find_element_by_name('lastname')
        element.send_keys(last_name)

    def schedule_demo(self):
        css = "input[value='Schedule Demo'][type='submit'] "
        element = self.browser.find_element_by_css_selector(css)
        element.click()

    def get_complete_all_required_fields_text(self):
        css = "div.hs_error_rollup ul li label"
        element = self.browser.find_element_by_css_selector(css)
        return element.text

