from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtility:

    def __init__(self, browser, timeout):
        self.wait = WebDriverWait(browser, timeout)

    def wait_for_element_to_be_interactable(self, locator_or_element):
        return self.wait.until(EC.element_to_be_clickable(locator_or_element))
    
    def wait_for_element_to_appear(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_all_elements_to_appear(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def wait_for_element_to_disappear(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def wait_for_element_removal(self, element):
        return self.wait.until(EC.staleness_of(element))

    def wait_for_child_element(self, parent, locator):
        element = self.wait.until(lambda _: parent.find_element(*locator))
        return element

    
