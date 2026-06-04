from selenium.webdriver.support.select import Select

class DropdownUtility:

    def __init__(self, browser):
        self.browser = browser

    def select_dropdown_visible_text(self, element, option):
        dropdown_element = Select(element)
        dropdown_element.select_by_visible_text(option)

    def get_all_selected_options(self, element):
        dropdown_element = Select(element)
        selected_options = dropdown_element.all_selected_options
        return list(map(lambda web_element : web_element.text, selected_options))