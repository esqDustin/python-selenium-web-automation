# Product Detail Test Case

## TC-DETAIL-001: Product Details On Display
**Test Case Description:** Verify detail page shows correct name and price for each product

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file
- Product details test data exist at `data/product_details.csv` and contains the name and price of each product

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv` 
- Product Info: name, price, id from `product_details.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. On the inventory page, identify and click on the product matching <name>.
5. Locate the product name and price elements on the detail page.

**Expected Result:**
- The URL updates to include the specific product ID (e.g. id=4) and matches <id> from the dataset.
- The displayed product name exactly matches <name> from the dataset.
- The displayed price exactly matches <price> from the dataset.

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_product_detail.py::test_product_details_on_display`