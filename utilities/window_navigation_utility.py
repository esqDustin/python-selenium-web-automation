
class WindowNavigation:

    def __init__(self, browser):
        self.browser = browser

    def window_go_back(self):
        self.browser.back()