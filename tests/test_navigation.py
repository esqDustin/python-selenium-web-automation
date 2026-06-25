import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.file_handling_ultility import read_csv_file

standard_login_credential = read_csv_file('data/general/standard_login_credential.csv')

@pytest.mark.testcase_id("TC-Nav-001")
@pytest.mark.nav
@pytest.mark.parametrize('login_data', standard_login_credential)
def test_nav_link_visibility(browser, utilities, login_data):
    
    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    inventory_page.click_on_burger_menu()
    
    expected_nav_links = ['All Items', 'About', 'Logout', 'Reset App State']

    assert inventory_page.are_burger_menu_links_showing() == True

    nav_links = inventory_page.get_burger_menu_links_name()

    assert nav_links == expected_nav_links

@pytest.mark.testcase_id("TC-Nav-002")
@pytest.mark.nav
@pytest.mark.parametrize('login_data', standard_login_credential)
def test_user_logout(browser, utilities, login_data):

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    inventory_page.click_on_burger_menu()
    inventory_page.click_on_burger_menu_link("Logout")
    
    login_page_url = login_page.get_login_page_url()

    assert login_page_url == 'https://www.saucedemo.com/'

    is_username_field_appeared = login_page.is_username_field_visible()

    assert is_username_field_appeared == True

@pytest.mark.testcase_id("TC-Nav-003")
@pytest.mark.nav
@pytest.mark.parametrize('login_data', standard_login_credential)
def test_back_button_inaccessible_after_logout(browser, utilities, login_data):

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    inventory_page.click_on_burger_menu()
    inventory_page.click_on_burger_menu_link("Logout")

    utilities.window_nav_helper.window_go_back()

    login_page_url = login_page.get_login_page_url()
    assert login_page_url == 'https://www.saucedemo.com/'

    login_error_message = login_page.get_login_error_message()
    assert login_error_message == "Epic sadface: You can only access '/inventory.html' when you are logged in."
