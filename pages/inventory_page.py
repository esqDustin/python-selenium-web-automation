from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class InventoryPage:
    
    inventory_header = (By.CSS_SELECTOR, '.app_logo')
    inventory_item = (By.CSS_SELECTOR, '.inventory_item')
    inventory_item_name = (By.CSS_SELECTOR, '.inventory_item_name ')
    inventory_item_price = (By.CSS_SELECTOR, '.inventory_item_price')
    inventory_item_image = (By.CSS_SELECTOR, 'a .inventory_item_img')
    inventory_sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    shopping_cart_link = (By.CSS_SELECTOR, '#shopping_cart_container a')
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
    burger_menu_button = (By.CLASS_NAME, 'bm-burger-button')
    burger_menu_wrap = (By.CLASS_NAME, 'bm-menu-wrap')
    burger_menu_links = (By.CLASS_NAME, 'menu-item')

    def __init__(self, broswer, utilities):
        self.browser = broswer
        self.wait_helper = utilities.wait_helper
        self.js_helper = utilities.js_helper
        self.dropdown_helper = utilities.dropdown_helper

    def get_inventory_page_url(self):
        return self.browser.current_url
    
    def is_shopping_cart_visible(self):
        try:
            self.wait_helper.wait_for_element_to_appear(self.shopping_cart_link)
            return True
        except TimeoutException:
            return False

    def get_inventory_items(self):
        return self.wait_helper.wait_for_all_elements_to_appear(self.inventory_item)
    
    def get_inventory_items_name(self):
        items = self.get_inventory_items()
        return list(map(lambda item : item.find_element(*self.inventory_item_name).text, items))
    
    def are_items_name_displayed(self):
        items = self.get_inventory_items()
        return list(map(lambda item : item.find_element(*self.inventory_item_name).is_displayed(), items))
    
    def are_items_displayed(self):
        items = self.get_inventory_items()
        return list(map(lambda item : item.is_displayed(), items))
    
    def get_inventory_items_price_as_text(self):
        items = self.get_inventory_items()
        return list(map(lambda item : item.find_element(*self.inventory_item_price).text, items))
    
    def get_inventory_items_price_as_numbers(self):
        items = self.get_inventory_items()
        text_prices_list = list(map(lambda item : item.find_element(*self.inventory_item_price).text, items))
        prices_to_float_list = [float(price.strip('$')) for price in text_prices_list]
        return prices_to_float_list
    
    def are_items_price_displayed(self):
        items = self.get_inventory_items()
        return list(map(lambda item : item.find_element(*self.inventory_item_price).is_displayed(), items))
    
    def are_items_image_displayed(self):
        items = self.get_inventory_items()
        return list(map(lambda item : 
                        self.js_helper.check_image_loaded_js(item.find_element(*self.inventory_item_image)), items))

    def get_inventory_page_header_text(self):
        return self.wait_helper.wait_for_element_to_appear(self.inventory_header).text
    
    def select_sort_option(self, option):
        dropdown_element = self.wait_helper.wait_for_element_to_be_interactable(self.inventory_sort_dropdown)
        self.dropdown_helper.select_dropdown_visible_text(dropdown_element, option)

    def get_selected_sort_option(self):
        dropdown_element = self.wait_helper.wait_for_element_to_be_interactable(self.inventory_sort_dropdown)
        return self.dropdown_helper.get_all_selected_options(dropdown_element)

    def get_item_based_on_price(self, position):
        price_list = self.get_inventory_items_price_as_numbers()
        return price_list[position]
    
    def get_item_based_on_name(self, position):
        name_list = self.get_inventory_items_name()
        return name_list[position]
    
    def click_on_product_card(self, product_name):
        inventory_item_link = (By.LINK_TEXT, product_name)
        product_clickable_card = self.wait_helper.wait_for_element_to_be_interactable(inventory_item_link)
        self.js_helper.click_js(product_clickable_card)

    def get_product_container(self, product_name):
        inventory_item = (By.XPATH, f"//div[@class ='inventory_item'][contains(., '{product_name}')]")
        item_container = self.wait_helper.wait_for_element_to_appear(inventory_item)
        return item_container

    def add_product_to_cart(self, product_name):
        item_container = self.get_product_container(product_name)
        add_to_cart_button = (By.TAG_NAME, 'button')
        self.wait_helper.wait_for_element_to_be_interactable(item_container.find_element(*add_to_cart_button)).click()

    def get_product_button_state_text(self, product_name):
        item_container = self.get_product_container(product_name)
        product_button = (By.TAG_NAME, 'button')
        state_text = self.wait_helper.wait_for_element_to_be_interactable(item_container.find_element(*product_button)).text
        return state_text
    
    def is_cart_badge_displayed(self):
        try:
            self.wait_helper.wait_for_element_to_appear(self.shopping_cart_badge)
            return True
        except TimeoutException:
            return False
        
    def get_amount_of_items_in_cart_badge(self):
        amount = self.wait_helper.wait_for_element_to_appear(self.shopping_cart_badge).text
        return int(amount)

    def click_on_shopping_cart(self):
        cart_element = self.wait_helper.wait_for_element_to_be_interactable(self.shopping_cart_link)
        cart_element.click()

    def click_on_burger_menu(self):
        bruger_menu = self.wait_helper.wait_for_element_to_be_interactable(self.burger_menu_button)
        bruger_menu.click()

    def are_burger_menu_links_showing(self):
        try:
            wrapper_element = self.wait_helper.wait_for_element_to_appear(self.burger_menu_wrap)
            return wrapper_element.get_attribute('aria-hidden') == "false"
        except TimeoutException:
            return False 
        
    def get_burger_menu_links_name(self):
        menu_links = self.wait_helper.wait_for_all_elements_to_appear(self.burger_menu_links)
        return list(map(lambda link : link.text, menu_links))
    
    def click_on_burger_menu_link(self, link_name):
        menu_links = self.wait_helper.wait_for_all_elements_to_appear(self.burger_menu_links)
        for menu_link in menu_links:
            if menu_link.text == link_name:
                self.wait_helper.wait_for_element_to_be_interactable(menu_link).click()
                break