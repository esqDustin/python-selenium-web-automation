from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CheckoutCompletePage:

    header_message = (By.CSS_SELECTOR, '.complete-header')
    body_message = (By.CSS_SELECTOR, '.complete-text')
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')

    def __init__(self, browser, utilities):
        self.browser = browser
        self.wait_helper = utilities.wait_helper

    def get_checkout_complete_url(self):
        return self.browser.current_url

    def get_confirmation_header_message(self):
        element = self.wait_helper.wait_for_element_to_appear(self.header_message)
        return element.text
    
    def get_confirmation_body_message(self):
        element = self.wait_helper.wait_for_element_to_appear(self.body_message)
        return element.text
    
    def is_shopping_cart_badge_not_displayed(self):
        try: 
            self.wait_helper.wait_for_element_to_disappear(self.shopping_cart_badge)
            return True
        except TimeoutException:
            return False
    

