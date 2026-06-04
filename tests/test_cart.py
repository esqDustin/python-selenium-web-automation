import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utilities.file_handling_ultility import read_csv_file, read_csv_file_with_lists

standard_login_credential = read_csv_file('data/general/standard_login_credential.csv')
item_shoplist = read_csv_file_with_lists('data/add_to_cart_items.csv', ['list_of_items'])
cart_operation_items = read_csv_file_with_lists('data/cart_operations.csv', ['list_of_added_items', 'list_of_removed_items'])

@pytest.mark.testcase_id("TC-Cart-001")
@pytest.mark.cart
@pytest.mark.parametrize('login_data', standard_login_credential)
def test_add_single_item_to_cart(browser, utilities, login_data):

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    inventory_page.add_product_to_cart('Sauce Labs Backpack')
    is_cart_badge_displayed = inventory_page.is_cart_badge_displayed()
    number_of_items_in_cart = inventory_page.get_amount_of_items_in_cart_badge()
    button_state_text = inventory_page.get_product_button_state_text('Sauce Labs Backpack')

    assert is_cart_badge_displayed is True, "Cart badge not displayed."
    assert number_of_items_in_cart == 1
    assert button_state_text.lower() == 'remove', "Cart state did not change from add... to remove"

@pytest.mark.testcase_id("TC-Cart-002")
@pytest.mark.cart
@pytest.mark.parametrize('login_data', standard_login_credential)
@pytest.mark.parametrize('items_to_add', item_shoplist)
def test_add_multiple_items_to_cart(browser, utilities, login_data, items_to_add):

    button_state_list = []

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)

    for item in items_to_add['list_of_items']:
        inventory_page.add_product_to_cart(item)
        button_state_list.append(inventory_page.get_product_button_state_text(item))

    is_cart_badge_displayed = inventory_page.is_cart_badge_displayed()
    number_of_items_in_cart = inventory_page.get_amount_of_items_in_cart_badge()
    
    assert is_cart_badge_displayed is True, "Cart badge not displayed."
    assert number_of_items_in_cart == len(items_to_add['list_of_items'])
    assert all(state.lower() == 'remove' for state in button_state_list)

@pytest.mark.testcase_id("TC-Cart-003")
@pytest.mark.cart
@pytest.mark.parametrize('login_data', standard_login_credential)
@pytest.mark.parametrize('cart_items', cart_operation_items)
def test_remove_items_in_cart(browser, utilities, login_data, cart_items):
    
    product_cards = []

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)

    for item in cart_items['list_of_added_items']:
        inventory_page.add_product_to_cart(item)

    inventory_page.click_on_shopping_cart()

    cart_page = CartPage(browser, utilities)

    for item in cart_items['list_of_removed_items']:
        product_card = cart_page.get_product_card_cart(item)
        product_cards.append(product_card)
        cart_page.remove_item_in_cart(item)
       
    is_cart_badge_displayed = cart_page.is_cart_badge_displayed()
    number_of_items_in_cart = cart_page.get_all_items_in_cart()

    if len(number_of_items_in_cart) > 0:
        cart_badge_item_amount = cart_page.get_amount_of_items_in_cart_badge()
        assert cart_badge_item_amount == len(number_of_items_in_cart)
        assert is_cart_badge_displayed is True
    else:
        assert len(number_of_items_in_cart) == 0
        assert is_cart_badge_displayed is False
    
    are_product_cards_removed = [cart_page.is_product_card_removed(card) for card in product_cards]
    assert all(is_removed is True for is_removed in are_product_cards_removed)
    
@pytest.mark.testcase_id("TC-Cart-004")
@pytest.mark.cart
@pytest.mark.parametrize('login_data', standard_login_credential)
@pytest.mark.parametrize('items_to_add', item_shoplist)
def test_cart_persistency(browser, utilities, login_data, items_to_add):
    
    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)

    for item in items_to_add['list_of_items']:
        inventory_page.add_product_to_cart(item)

    inventory_page.click_on_shopping_cart()

    cart_page = CartPage(browser, utilities)
    number_of_items_in_badge = cart_page.get_amount_of_items_in_cart_badge()
    items_in_cart = cart_page.get_all_items_in_cart()

    assert number_of_items_in_badge == len(items_in_cart)

    cart_page.click_on_continue_shopping()
   
    is_cart_badge_displayed = inventory_page.is_cart_badge_displayed()
    bagde_count_items = inventory_page.get_amount_of_items_in_cart_badge()

    assert is_cart_badge_displayed is True
    assert bagde_count_items == len(items_in_cart)