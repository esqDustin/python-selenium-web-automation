# Inventory Test Case

## TC-INVENTORY-001: Inventory Products On Display
**Test Case Description:** Verify the six products are displayed correctly on the inventory page

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv`
- Valid credentials exist in the test data file

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv` 

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button

**Expected Result:**
- URL redirects to https://www.saucedemo.com/inventory.html.
- Exactly six product cards are visible in the product grid
- For each product card:
   - Product name is visible and not empty
   - Product price is visible and starts with "$"
   - Product image has loaded (no broken image)

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_inventory.py::test_inventory_products_on_display`

---

## TC-INVENTORY-002: Sort Products By Price (low to high)
**Test Case Description:** Verify that the prodcuts are displayed from lowest to highest price

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv`
- Valid credentials exist in the test data file

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv` 

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Click the product sort dropdown in the inventory page
5. Select "Price (low to high)"

**Expected Result:**
- URL redirects to https://www.saucedemo.com/inventory.html.
- The dropdown displays "Price (low to high)" as the active sorting method.
- The list of prices is in ascending numerical order (each price is less than or equal to the price that follows it).
- The first item displayed has the minimum price in the set, and the last item has the maximum price.

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_inventory.py::test_sort_products_by_low_to_high_price`

--- 

## TC-INVENTORY-003: Sort Products By Name (Z to A)
**Test Case Description:** Verify the products are displayed in alphabetical order from Z to A

**Preconditions:**
- TTest data file exists at `data/general/standard_login_credential.csv`
- Valid credentials exist in the test data file

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv` 

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Click on the product sort dropdown in the inventory page
5. Select "Name (Z to A)" 
6. Collect all of the displayed product names

**Expected Result:**
- URL redirects to https://www.saucedemo.com/inventory.html.
- The dropdown displays "Name (Z to A)" as the active sorting method.
- The list of names is in descending alphabetical order.
- The product with the name closest to "Z" appears first; the product closest to "A" appears last

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_inventory.py::test_sort_products_by_Z_to_A_name`