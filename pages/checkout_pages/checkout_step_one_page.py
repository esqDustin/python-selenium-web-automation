from selenium.webdriver.common.by import By

class CheckoutStepOnePage:

    first_name_input_field = (By.ID, "first-name")
    last_name_input_field = (By.ID, "last-name")
    postal_code_input_field = (By.ID, "postal-code")
    continue_checkout_button = (By.ID, "continue") 
    error_message = (By.CSS_SELECTOR, '.error-message-container h3')
    input_error_icon = (By.CSS_SELECTOR, '.error_icon')

    def __init__(self, browser, utilities):
        self.browser = browser
        self.wait_helper = utilities.wait_helper

    def get_checkout_step_one_page_url(self):
        return self.browser.current_url

    def input_first_name(self, name):
        element = self.wait_helper.wait_for_element_to_be_interactable(self.first_name_input_field)
        element.clear()
        element.send_keys(name)

    def input_last_name(self, name):
        element = self.wait_helper.wait_for_element_to_be_interactable(self.last_name_input_field)
        element.clear()
        element.send_keys(name)

    def input_postal_code(self, postal_code):
        element = self.wait_helper.wait_for_element_to_be_interactable(self.postal_code_input_field)
        element.clear()
        element.send_keys(postal_code)

    def click_continue_button(self):
        self.wait_helper.wait_for_element_to_be_interactable(self.continue_checkout_button).click()

    def get_incomplete_info_error_message(self):
       return self.wait_helper.wait_for_element_to_appear(self.error_message).text
    
    def get_error_icons(self):
        return self.wait_helper.wait_for_all_elements_to_appear(self.input_error_icon)
        