---
title: "QA Automation Challenge"
author: "Marek kaminski"
date: "2025-08-29"
tags: ["QA", "UI Testing", "Playwright", "Pytest", "Sauce Demo"]
---


# QA Automation Challenge - Senior QA Engineer

## Project Overview
This project contains **UI test automation** for the Sauce Demo application ([https://www.saucedemo.com](https://www.saucedemo.com)) using **Playwright** and **Pytest**.  
It demonstrates the ability to design, write, and execute automated UI tests for critical application functionality.

---

## Features Tested
1. **Login with valid credentials**
   - Verifies that a user can log in successfully.
2. **Login with invalid credentials**
   - Verifies that login fails with incorrect credentials and shows an error message.

---

## Project Structure
QA-challenge/
├── pages/
│ ├── __init__.py
│ └── login_page.py # Page Object Model for the Login page
├── tests/
│ ├── __init__.py
│ └── test_login.py # Automated UI test cases
├── TestCases.md # Test design and strategy document
├── requirements.txt # Required Python packages
└── README.md # This file

---

## Prerequisites

- **Python 3.10+** installed
- Pip package manager
- Internet access (to visit Sauce Demo and download browser binaries)
- Supported OS: Windows, macOS, or Linux

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/kmarek0415-ai/QA-challenge.git
cd QA-challenge

2. **Install dependencies**

```bash
pip install -r requirements.txt
playwright install

3. **Run the tests**

```bash
pytest -v

