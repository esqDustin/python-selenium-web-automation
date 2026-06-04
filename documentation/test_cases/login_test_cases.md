# Login Test Cases

## TC-LOGIN-001: Valid Login
**Test Case Description:** Verify user can login with valid credentials

**Preconditions:**
- User is on login page
- Test data file `data/valid_login_credentials.csv` exists and contains valid credentials

**Test Data:** 
- Credentials: username and password from `valid_login_credentials.csv`

**Test Steps:**
1. Go to "https://www.saucedemo.com/"
2. Enter <username> from the dataset
3. Enter <password> from the dataset
4. Click "Login" button

**Expected Result:**
- URL redirects to https://www.saucedemo.com/inventory.html.
- The text 'Swag Labs' is displayed in the primary header.
- The shopping cart container element is visible.

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_login.py::test_successful_login`

---

## TC-LOGIN-002: Invalid Login
**Test Case Description:** Verify user cannot login with invalid credentials or incomplete information

**Preconditions:**
- User is on login page
- Test data file `data/invalid_login_credentials.csv` exists and contains invalid credentials

**Test Data:** 
- Credentials: username and password from `invalid_login_credentials.csv`
- Error Message: error_message from `invalid_login_credentials.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click the "Login" button

**Expected Result:**
- The error message text exactly matches <error_message> of the `invalid_login_credentials.csv`.
- Error icons appear within the input fields.
- The URL remains at https://www.saucedemo.com/.

**Status:** PASS

**Automated:** Yes
**Automation Reference:** `tests/test_login.py::test_unsuccessful_login`