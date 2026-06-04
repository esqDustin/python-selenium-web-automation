import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.file_handling_ultility import read_csv_file

standrard_login_credential = read_csv_file('data/general/standard_login_credential.csv')

@pytest.mark.testcase_id("TC-INVENTORY-001")
@pytest.mark.inventory
@pytest.mark.parametrize('login_data', standrard_login_credential)
def test_inventory_products_on_display(browser, utilities, login_data):
    
    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    items = inventory_page.get_inventory_items()
    are_items_displayed = inventory_page.are_items_displayed()
    are_items_name_displayed = inventory_page.are_items_name_displayed()
    item_names = inventory_page.get_inventory_items_name()
    are_items_price_displayed = inventory_page.are_items_price_displayed()
    item_prices = inventory_page.get_inventory_items_price_as_text()
    are_items_image_displatyd = inventory_page.are_items_image_displayed()

    assert 'inventory.html' in inventory_page.get_inventory_page_url()
    assert len(items) == 6
    assert all(displayed_item is True for displayed_item in are_items_displayed)
    assert all(displayed_item_name is True for displayed_item_name in are_items_name_displayed)
    assert all(name != '' for name in item_names)
    assert all(displayed_item_price is True for displayed_item_price in are_items_price_displayed)
    assert all(price.startswith('$') for price in item_prices)
    assert all(item_image_displayed is True for item_image_displayed in are_items_image_displatyd)

@pytest.mark.testcase_id("TC-INVENTORY-002")
@pytest.mark.inventory
@pytest.mark.parametrize('login_data', standrard_login_credential)
def test_sort_products_by_low_to_high_price(browser, utilities, login_data):
    
    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    item_prices_before_sorting = inventory_page.get_inventory_items_price_as_numbers()
    inventory_page.select_sort_option('Price (low to high)')
    item_prices_after_sorting = inventory_page.get_inventory_items_price_as_numbers()
    lowest_price = inventory_page.get_item_based_on_price(0)
    highest_price = inventory_page.get_item_based_on_price(-1)

    assert 'inventory.html' in inventory_page.get_inventory_page_url()
    assert 'Price (low to high)' in inventory_page.get_selected_sort_option()
    assert item_prices_after_sorting == sorted(item_prices_before_sorting)
    assert lowest_price == 7.99
    assert highest_price == 49.99

@pytest.mark.testcase_id("TC-INVENTORY-003")
@pytest.mark.inventory
@pytest.mark.parametrize('login_data', standrard_login_credential)
def test_sort_products_by_Z_to_A_name(browser, utilities, login_data):
    
    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    item_names_before_sorting = inventory_page.get_inventory_items_name()
    inventory_page.select_sort_option('Name (Z to A)')
    item_names_after_sorting = inventory_page.get_inventory_items_name()
    first_product_name = inventory_page.get_item_based_on_name(0)
    last_product_name = inventory_page.get_item_based_on_name(-1)

    assert 'inventory.html' in inventory_page.get_inventory_page_url()
    assert 'Name (Z to A)' in inventory_page.get_selected_sort_option()
    assert item_names_after_sorting == sorted(item_names_before_sorting, reverse=True)
    assert first_product_name == 'Test.allTheThings() T-Shirt (Red)'
    assert last_product_name == 'Sauce Labs Backpack'