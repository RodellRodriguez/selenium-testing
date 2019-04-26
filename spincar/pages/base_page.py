class BasePage(object):
    def __init__ (self, browser):
        self.browser = browser
        self.timeout = 10