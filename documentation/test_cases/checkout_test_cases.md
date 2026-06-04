# Checkout Test Case

## TC-CHECKOUT-001: Full Happy-path Purchase
**Test Case Description:** Verify the purchase confirmation message after the user completed a successful end-to-end purchase

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file
- Sample customer info file exists at `data/general/sample_customer_info.csv` with each of the fields are filled

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`
- Customer Info: first name, last name, zip code from `sample_customer_info.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Choose one of the six products (e.g. "Sauce Labs Backpack") in the inventory page
5. Click the "Add to cart" button
6. Click the "Shopping Cart" icon to navigate to the cart page
7. In the cart page, click on the "Checkout" button
8. Fill in the checkout form with the following values:
   - First Name: <first_name>
   - Last Name: <last_name>
   - Zip/Postal Code: <zip_code>
9. Click on the "Continue" button in the checkout step one page
10. Click on the "Finish" button in the checkout step two page

**Expected Result:**
- The product (e.g. "Sauce Labs Backpack") is visible in the cart list prior to clicking Checkout.
- The user is redirected to https://www.saucedemo.com/checkout-complete.html
- The shopping cart badge is cleared (displays no number).
- The confirmation message is displayed and it entails: 
    - Header: "Thank you for your order!"
    - Body: "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_checkout.py::test_checkout_happy_path`

--- 

## TC-CHECKOUT-002: Empty Cart Checkout
**Test Case Description:** Verify that the user is prohibitied in continuing from checking out with an empty cart

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Click the "Shopping Cart" icon in the inventory page
5. Attempt clicking the "Checkout" button in the cart page

**Expected Result:**
- The user should stay in the cart page (https://www.saucedemo.com/cart.html) and blocked from proceeding to the checkout process. 
- A validation message or disabled "Checkout" button should prevent the user on continuing the checkout flow.

**Actual Result:**
- The checkout button is not disabled.
- The user can still complete the whole checkout process despite having an empty cart.

**Status:** FAIL
**Bug Reference:** `BUG-Cart-001` from `documentation/bug_reports/cart_bug_reports.md`

**Automated:** Yes
**Automation Reference:** `tests/test_checkout.py::test_empty_cart_checkout`

--- 

## TC-CHECKOUT-003: Incomplete Checkout Information
**Test Case Description:** Verify the error message(s) for incomplete customer information on checkout

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file
- Incomplete customer info test data exists: `data/incomplete_customer_info.csv`

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`
- Customer Info: first_name, last_name, and zip-code from `incomplete_customer_info.csv`
- Error Message: error_message from `incomplete_customer_info.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Choose one of the six products (e.g. "Sauce Labs Backpack") in the inventory page
5. Click the "Add to cart" button
6. Click the "Shopping Cart" icon to navigate to the cart page
7. In the cart page, click on the "Checkout" button
8. Fill in the checkout form with the following values:
   - First Name: <first_name>
   - Last Name: <last_name>
   - Zip/Postal Code: <zip_code>
9. Click on the "Continue" button in the checkout step one page


**Expected Result:**
- The product (e.g. "Sauce Labs Backpack") is visible in the cart list prior to clicking Checkout.
- The user is blocked from continuing the checkout process and should stay at https://www.saucedemo.com/checkout-step-one.html.
- An <error_message> should be displayed containing what customer information has been missed.
- Error icons appear within the input fields.

**Status:** PASS

**Automated:** Yes
**Automation Reference:**  `tests/test_checkout.py::test_incomplete_customer_info_checkout`