from selenium.webdriver.common.by import By

class CheckoutStepTwoPage:

    finish_checkout_button = (By.ID, "finish")

    def __init__(self, browser, utitlities):
        self.browser = browser
        self.wait_helper = utitlities.wait_helper

    def click_on_finish_checkout_button(self):
        self.wait_helper.wait_for_element_to_be_interactable(self.finish_checkout_button).click()