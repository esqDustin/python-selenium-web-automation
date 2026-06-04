from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException

class LoginPage:

    username_input_field = (By.ID, 'user-name')
    password_input_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    error_message = (By.CSS_SELECTOR, '.error-message-container h3')
    input_error_icon = (By.CSS_SELECTOR, '.error_icon')

    URL = 'https://www.saucedemo.com/'

    def __init__(self, browser, utilities):
        self.browser = browser
        self.wait_helper = utilities.wait_helper

    def load(self):
        self.browser.get(self.URL)

    def enter_username(self, username):
        element = self.wait_helper.wait_for_element_to_be_interactable(self.username_input_field)
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait_helper.wait_for_element_to_be_interactable(self.password_input_field)
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        button = self.wait_helper.wait_for_element_to_be_interactable(self.login_button)
        button.click()

    def is_username_field_visible(self):
        try:
            self.wait_helper.wait_for_element_to_appear(self.username_input_field)
            return True
        except TimeoutException:
            return False
            
    def get_login_error_message(self):
        return self.wait_helper.wait_for_element_to_appear(self.error_message).text
    
    def get_error_icons(self):
        return self.wait_helper.wait_for_all_elements_to_appear(self.input_error_icon)
    
    def get_login_page_url(self):
        return self.browser.current_url

    