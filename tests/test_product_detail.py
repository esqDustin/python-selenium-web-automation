import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_detail_page import ProductDetailsPage
from utilities.file_handling_ultility import read_csv_file
import re

standrard_login_credential = read_csv_file('data/general/standard_login_credential.csv')
product_info = read_csv_file('data/product_details.csv')

@pytest.mark.testcase_id("TC-DETAIL-001")
@pytest.mark.product_detail
@pytest.mark.parametrize('login_data', standrard_login_credential)
@pytest.mark.parametrize('product_details', product_info)
def test_product_details_on_display(browser, utilities, login_data, product_details):

    login_page = LoginPage(browser, utilities)
    login_page.load()

    login_page.enter_username(login_data['username'])
    login_page.enter_password(login_data['password'])
    login_page.click_login_button()

    inventory_page = InventoryPage(browser, utilities)
    inventory_page.click_on_product_card(product_details['name'])

    product_details_page = ProductDetailsPage(browser, utilities)
    product_name = product_details_page.get_product_name()
    product_price = product_details_page.get_product_price()
    product_url = product_details_page.get_product_url()

    regex_pattern = r'id=(\d+)'
    match = re.search(regex_pattern, product_url)
    actual_url_id = match.group(1)

    assert match, f"URL pattern is incorrect. 'id=' parameter not found in {product_url}"
    assert actual_url_id == product_details['product_id']
    assert product_name == product_details['name']
    assert product_price == product_details['price']