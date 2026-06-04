from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class CartPage:

    checkout_button = (By.ID, "checkout")
    cart_items = (By.CLASS_NAME, "cart_item")
    item_name = (By.CLASS_NAME, "inventory_item_name")
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    continue_shopping_button = (By.ID, "continue-shopping")

    def __init__(self, browser, utilities):
        self.browser = browser
        self.wait_helper = utilities.wait_helper

    def get_cart_page_url(self):
        return self.browser.current_url

    def get_all_items_in_cart(self):
        try: 
            items_in_cart = self.wait_helper.wait_for_all_elements_to_appear(self.cart_items)
            return items_in_cart
        except TimeoutException:
            return []
    
    def get_all_item_names_in_cart(self):
        items = self.get_all_items_in_cart()
        if len(items) > 0:
            return list(map(lambda item : item.find_element(*self.item_name).text, items))
        else:
            return []

    def click_on_checkout_button(self):
        self.wait_helper.wait_for_element_to_be_interactable(self.checkout_button).click()

    def is_checkout_button_disabled(self):
        element = self.wait_helper.wait_for_element_to_appear(self.checkout_button)
        return not element.is_enabled()
    
    def get_product_card_cart(self, product_name):
        prodcut_card_xpath = f"//div[@class='cart_item'][contains(., '{product_name}')]"
        product_card = (By.XPATH, prodcut_card_xpath)
        card_element = self.wait_helper.wait_for_element_to_appear(product_card)
        return card_element

    def is_product_card_removed(self, product_card_element):
         return "removed_cart_item" in product_card_element.get_attribute("class")
        
    def remove_item_in_cart(self, product_name):
        product_card = self.get_product_card_cart(product_name)
        name = "-".join(product_name.lower().split())
        remove_button_locator = (By.ID, f'remove-{name}')
        self.wait_helper.wait_for_element_to_be_interactable(product_card.find_element(*remove_button_locator)).click()

    def is_cart_badge_displayed(self):
        try:
            self.wait_helper.wait_for_element_to_appear(self.shopping_cart_badge)
            return True
        except TimeoutException:
            return False

    def get_amount_of_items_in_cart_badge(self):
        amount = self.wait_helper.wait_for_element_to_appear(self.shopping_cart_badge).text
        return int(amount)
    
    def click_on_continue_shopping(self):
        self.wait_helper.wait_for_element_to_be_interactable(self.continue_shopping_button).click()

