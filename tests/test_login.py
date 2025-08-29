import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False lets you see the browser
        page = browser.new_page()
        login = LoginPage(page)

        login.goto()
        login.login("standard_user", "secret_sauce")

        assert "inventory.html" in page.url

        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login = LoginPage(page)

        login.goto()
        login.login("invalid_user", "wrong_password")

        error_message = page.inner_text("h3[data-test='error']")
        assert "Epic sadface" in error_message

        browser.close()
