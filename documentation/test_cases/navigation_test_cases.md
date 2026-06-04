## TC-Nav-001: Burger Menu Nav Links
**Test Case Description:** Verify the navigation links are visible after clicking the burger menu.

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file.

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Click on the burger menu

**Expected Result:**
- The burger menu should open and display the following navigation links:
  - All Items
  - About
  - Logout
  - Reset App State

**Status:** PASS

**Automated:** Yes

**Automation Reference:** `tests/test_navigation.py::test_nav_link_visibility`

---

## TC-Nav-002: User Logout
**Test Case Description:** Verify the user is navigated back to the login page after logging out

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file.

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Click on the burger menu
5. Click on the "Logout" button

**Expected Result:**
- URL redirects to https://www.saucedemo.com/
- The login page is displayed (username input field is visible).

**Status:** PASS

**Automated:** Yes

**Automation Reference:** `tests/test_navigation.py::test_user_logout`

---

## TC-Nav-003: Prevent Access After User Logout
**Test Case Description:** Verify the inventory page is inaccessible when navigating backwards via the browser history after logging out

**Preconditions:**
- Test data file exists at `data/general/standard_login_credential.csv` and valid credentials exist in the test data file.

**Test Data:** 
- Credentials: username and password from `standard_login_credential.csv`

**Test Steps:**
1. Navigate to "https://www.saucedemo.com/"
2. Enter <username> and <password> from the dataset
3. Click "Login" button
4. Click on the burger menu
5. Click on the "Logout" button
6. Click on the browser's native back button

**Expected Result:**
- The user should be blocked from viewing the inventory page.
- The user should remain on/be returned to the login page (https://www.saucedemo.com/) after triggering history navigation.
- An authentication error message container should display: "Epic sadface: You can only access '/inventory.html' when you are logged in."

**Status:** PASS

**Automated:** Yes

**Automation Reference:** `tests/test_navigation.py::test_back_button_inaccessible_after_logout`
