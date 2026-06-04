import pytest
import json
import selenium.webdriver
from utilities.wait_utility import WaitUtility
from utilities.dropdown_utility import DropdownUtility
from utilities.js_utility import JavascriptUtility
from utilities.window_navigation_utility import WindowNavigation
from utilities.utility_bundle import UtilityBundle

@pytest.fixture(scope='session')
def config():

    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome']
    
    return config

@pytest.fixture(scope='function')
def browser(config):
  
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()

    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()

    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)

    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()

@pytest.fixture(scope='function')
def wait_helper(browser, config):
    return WaitUtility(browser, config['explicit_wait'])

@pytest.fixture(scope='function')
def dropdown_helper(browser):
    return DropdownUtility(browser)

@pytest.fixture(scope='function')
def js_helper(browser):
    return JavascriptUtility(browser)

@pytest.fixture(scope='function')
def window_nav_helper(browser):
    return WindowNavigation(browser)

@pytest.fixture(scope='function')
def utilities(wait_helper, js_helper, dropdown_helper, window_nav_helper):
    return UtilityBundle(wait_helper, js_helper, dropdown_helper, window_nav_helper)