import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.file_handling_ultility import read_csv_file

valid_credentials = read_csv_file('data/valid_login_credentials.csv')
invalid_credentials = read_csv_file('data/invalid_login_credentials.csv')

@pytest.mark.testcase_id("TC-LOGIN-001")
@pytest.mark.login
@pytest.mark.parametrize('test_data', valid_credentials)
def test_successful_login(browser, utilities, test_data):

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(test_data['username'])
    login_page.enter_password(test_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)

    assert test_data['header_phrase'] in inventory_page.get_inventory_page_header_text()
    assert test_data['partial_url_link'] in inventory_page.get_inventory_page_url()
    assert inventory_page.is_shopping_cart_visible() == True


@pytest.mark.testcase_id("TC-LOGIN-002")
@pytest.mark.login
@pytest.mark.parametrize('test_data', invalid_credentials)
def test_unsuccessful_login(browser, utilities, test_data):
    
    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(test_data['username'])
    login_page.enter_password(test_data['password'])
    login_page.click_login_button()

    assert test_data['error_message'] in login_page.get_login_error_message()
    assert test_data['full_url_link'] == login_page.get_login_page_url()
    assert len(login_page.get_error_icons()) > 0