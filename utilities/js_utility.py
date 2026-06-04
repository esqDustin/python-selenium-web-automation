class JavascriptUtility:

    def __init__(self, browser):
        self.browser = browser

    def check_image_loaded_js(self, element):
        is_loaded = self.browser.execute_script("return arguments[0].naturalWidth > 0", element)
        return is_loaded
    
    def scroll_into_view_js(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_js(self, element):
        self.browser.execute_script("arguments[0].click();", element)
    

