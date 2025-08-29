# Test Design Document

## Application
[https://www.saucedemo.com/](https://www.saucedemo.com/)

## Feature to Test
Login functionality

---

### Test Case 1: Valid Login
**Description**: Verify that a user can log in with valid credentials.  
**Steps**:
1. Navigate to login page
2. Enter username: `standard_user`
3. Enter password: `secret_sauce`
4. Click login button
**Expected Result**: User is redirected to `inventory.html` page.

---

### Test Case 2: Invalid Login
**Description**: Verify that login fails with incorrect credentials.  
**Steps**:
1. Navigate to login page
2. Enter username: `invalid_user`
3. Enter password: `wrong_password`
4. Click login button
**Expected Result**: Error message `Epic sadface: Username and password do not match` is displayed.
