# Cart Bug Reports

## BUG-Cart-001: Empty cart checkout not blocked

**Description:** The checkout button remains active and clickable when the shopping cart is empty, allowing users to proceed with the checkout process.

**Environment:** Chrome (Latest), Firefox (Latest) / macOS

**Steps to Reproduce:** 
1. Navigate to the SauceDemo login page.
2. Enter valid credentials:
    - Username: standard_user
    - Password: secret_sauce
3. Click the "Login" button
4. Click the "Shopping Cart" icon in the top right corner to open the cart page.
5. Observe the Checkout button, and click it.

**Expected:**
- The checkout button should be disabled or a validation message should be present that prevents the user from continuing the checkout flow.

**Actual:** 
- The checkout button remains active. Clicking on the checkout button allows the user to complete the whole checkout flow with an empty cart.

**Severity:** Medium