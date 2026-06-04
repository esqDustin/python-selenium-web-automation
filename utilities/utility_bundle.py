
# used as a container for the utitlites fixtures to be used on page objects
class UtilityBundle:
    def __init__(self, wait_helper, js_helper=None, dropdown_helper=None, window_nav_helper=None):
        self.wait_helper = wait_helper
        self.js_helper = js_helper
        self.dropdown_helper = dropdown_helper
        self.window_nav_helper = window_nav_helper