
🚀 Features
1. 🔐 Login Automation
✅ Login with valid credentials and verify access to the inventory page.

❌ Attempt login with invalid user and 
verify that an error message is displayed.

2. 🛒 Cart Functionality
➕ Add at least two products to the shopping cart.

✔️ Verify the products were successfully added.

➖ Remove one product and confirm that the cart updates correctly.

3. 🎁 Optional Bonus Tests
🔄 Filter or sort products by name or price.

📊 Verify that product order changes as expected.

🛠️ Technologies Used
Language: Python 3.12.0

Testing Library: unittest (standard library)

Browser Automation: Selenium WebDriver

Browser: Chrome (via ChromeDriver)

Pattern: Page Object Model (Only Login)


Install dependencies

pip install -r requirements.txt

Download ChromeDriver
Make sure the version matches your Chrome browser and place it in the drivers/ folder.

Requirements:

pytest==8.3.5
selenium==4.31.0
webdriver-manager==4.0.2
pytest-html==4.1.1


▶️ Running the Tests
   positive: All positive Selenium test
   negative: All negative test
   addproduct: All products added test
   filter: search by filter test
   removeproduct: Removed product