import re
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_pages.checkout_complete_page import CheckoutCompletePage
from utilities.file_handling_ultility import read_csv_file

standard_login_credential = read_csv_file('data/general/standard_login_credential.csv')
sample_customer_info = read_csv_file('data/general/single_customer_info.csv')
incomplete_customer_info = read_csv_file('data/incomplete_customer_info.csv')

@pytest.mark.testcase_id("TC-CHECKOUT-001")
@pytest.mark.checkout
@pytest.mark.parametrize('login_data', standard_login_credential)
@pytest.mark.parametrize('customer_data', sample_customer_info)
def test_checkout_happy_path(browser, utilities, login_data, customer_data):

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    inventory_page.add_product_to_cart('Sauce Labs Backpack')
    inventory_page.click_on_shopping_cart()

    cart_page = CartPage(browser, utilities)
    cart_item_names = cart_page.get_all_item_names_in_cart()

    assert "Sauce Labs Backpack" in cart_item_names

    cart_page.click_on_checkout_button()

    checkout_step_one_page = CheckoutStepOnePage(browser, utilities)
    checkout_step_one_page.input_first_name(customer_data['first_name'])
    checkout_step_one_page.input_last_name(customer_data['last_name'])
    checkout_step_one_page.input_postal_code(customer_data['zip_code'])
    checkout_step_one_page.click_continue_button()

    checkout_step_two_page = CheckoutStepTwoPage(browser, utilities)
    checkout_step_two_page.click_on_finish_checkout_button()

    checkout_complete_page = CheckoutCompletePage(browser, utilities)
    header_message = checkout_complete_page.get_confirmation_header_message()
    body_message = checkout_complete_page.get_confirmation_body_message()
    checkout_complete_url = checkout_complete_page.get_checkout_complete_url()
    is_shopping_cart_badge_gone = checkout_complete_page.is_shopping_cart_badge_not_displayed()

    regex_pattern = r"/checkout-complete\.html$"
    match = re.search(regex_pattern, checkout_complete_url)

    assert match, f'There is a mismatch between the regex pattern and the actual url.'
    assert is_shopping_cart_badge_gone == True, 'Shopping cart badge still on display.'
    assert header_message == 'Thank you for your order!'
    assert body_message == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'

@pytest.mark.testcase_id("TC-CHECKOUT-002")
@pytest.mark.xfail(reason='Bug: SauceDemo allows checkout with an empty cart, should be blocked')
@pytest.mark.checkout
@pytest.mark.parametrize('login_data', standard_login_credential)
def test_empty_cart_checkout(browser, utilities, login_data):
    
    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    inventory_page.click_on_shopping_cart()

    cart_page = CartPage(browser, utilities)
    is_checkout_disabled = cart_page.is_checkout_button_disabled()

    assert is_checkout_disabled == True, 'Checkout button is still enabled.'

    cart_page.click_on_checkout_button()
    cart_page_url = cart_page.get_cart_page_url()

    regex_pattern = r'/cart\.html$'
    match = re.search(regex_pattern, cart_page_url)
    assert match, 'The user is still redirected to the checkout page'

@pytest.mark.testcase_id("TC-CHECKOUT-003")
@pytest.mark.checkout
@pytest.mark.parametrize('login_data', standard_login_credential)
@pytest.mark.parametrize('customer_data', incomplete_customer_info)
def test_incomplete_customer_info_checkout(browser, utilities, login_data, customer_data):

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    inventory_page.add_product_to_cart('Sauce Labs Backpack')
    inventory_page.click_on_shopping_cart()

    cart_page = CartPage(browser, utilities)
    cart_item_names = cart_page.get_all_item_names_in_cart()

    assert "Sauce Labs Backpack" in cart_item_names

    cart_page.click_on_checkout_button()

    checkout_step_one_page = CheckoutStepOnePage(browser, utilities)
    checkout_step_one_page.input_first_name(customer_data['first_name'])
    checkout_step_one_page.input_last_name(customer_data['last_name'])
    checkout_step_one_page.input_postal_code(customer_data['zip_code'])
    checkout_step_one_page.click_continue_button()

    error_icons = checkout_step_one_page.get_error_icons()
    error_message = checkout_step_one_page.get_incomplete_info_error_message()
    checkout_step_one_page_url = checkout_step_one_page.get_checkout_step_one_page_url()

    regex_parttern = r'/checkout-step-one\.html$'
    match = re.search(regex_parttern, checkout_step_one_page_url)

    assert match, "Actual link does not match with the regex pattern"
    assert len(error_icons) > 0, "Visual error icons are missing."
    assert error_message == customer_data['error_message'], "Actual error message does not match with the expected message."
