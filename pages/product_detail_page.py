from selenium.webdriver.common.by import By

class ProductDetailsPage:

    product_name = (By.CLASS_NAME, 'inventory_details_name')
    product_price = (By.CLASS_NAME, 'inventory_details_price')

    def __init__(self, browser, utilities):
        self.browser = browser
        self.wait_helper = utilities.wait_helper

    def get_product_url(self):
        return self.browser.current_url

    def get_product_name(self):
        return self.wait_helper.wait_for_element_to_appear(self.product_name).text

    def get_product_price(self):
        return self.wait_helper.wait_for_element_to_appear(self.product_price).text
    
        