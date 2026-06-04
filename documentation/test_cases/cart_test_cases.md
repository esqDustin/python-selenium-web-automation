# Cart Test Case

## TC-Cart-001: Add Single Item to Cart
**Test Case Description:** Verify cart badge updates to 1 after adding a single item to cart

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Choose one of the six products (e.g. "Sauce Labs Backpack") in the inventory page
5. Click the "Add to cart" button

**Expected Result:**
- The product button state text should change from "Add to cart" to "Remove".
- The cart badge should be present.
- The number shown in the cart badge should display "1" immediately after add a single item to cart.

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_cart.py::test_add_single_item_to_cart`

---

## TC-Cart-002: Add Multiple Items to Cart
**Test Case Description:** Verify cart badge updates to the number of items added to cart

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file
- Test data file exists at `data/add_to_cart_items.csv` and the list of items to be added exists

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`
- Items to Cart: list_of_items from `add_to_cart_items.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Choose the products based on <list_of_items> from the `add_to_cart_items.csv` in the inventory page.
5. Click the "Add to cart" button for each of the corresponding products

**Expected Result:**
- The button state for each selected product should change to 'Remove'.
- The cart badge should be present.
- The number shown in the cart badge should display the number of added items in cart.

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_cart.py::test_add_multiple_items_to_cart`

---

## TC-Cart-003: Remove Item(s) From Cart
**Test Case Description:** Verify the product card disappears and updates the number of items in cart after removal

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file
- Test data file exists at `data/cart_operations.csv` and the list of items to be added and removed exists

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`
- Items to cart: list_of_added_items from `cart_operations.csv`
- Items to remove: list_of_removed_items from `cart_operations.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Choose the products based on <list_of_added_items> from the `cart_operations.csv` in the inventory page.
5. Click the "Shopping Cart" icon to navigate to the cart page
6. In the cart page, click "Remove" button on the product cards of each item based on <list_of_removed_items> from `cart_operations.csv`

**Expected Result:**
- The product card of the item should be gone from the cart after removal.
- The cart badge should be present or removed based on the count of items in cart. The cart badge should be removed when the cart is empty. In contrast, the badge should be present if the cart is not empty.
- The number shown in the cart badge should update and reflect the remaining items in cart.

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_cart.py::test_remove_items_in_cart`

---

## TC-Cart-004: Cart Persistency
**Test Case Description:** Verify the cart persists after navigating back to the inventory page.

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file
- Test data file exists at `data/add_to_cart_items.csv` and the list of items to be added exists

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`
- Items to Cart: list_of_items from `add_to_cart_items.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Add the products to cart based on <list_of_items> from the `add_to_cart_items.csv` in the inventory page.
5. Click the "Shopping Cart" icon to navigate to the cart page
6. In the cart page, click "Continue Shopping" button to navigate back to inventory page.

**Expected Result:**
- The number of items in the cart page should match the badge count
- After navigating back to the inventory page, the cart badge should still be present
- The badge count on the inventory page should match the number of items added

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_cart.py::test_cart_persistency`