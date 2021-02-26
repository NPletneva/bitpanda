# test_task_bp
This project is Test Automation Engineer Assessment.
- all tests are in MyStoreTest.py - test’s scripts
- StoreBase.py - basic accessor methods for elements, contains methods common for all tests
- LoginFlowTestCase.py - contains methods/locators specific for login flow test
- AccountTestCase - contains methods/locators specific for account test
- CartTestCase - contains methods/locators specific for order cart tests
- CatalogTestCase - contains methods/locators specific for catalog tests
- all data are in config.yml
- ci.yml - configuration setup to run tests in a ci

You can check all testruns history thru 'Actions' section here in GitHub.


test_create_account
- open main page
- go to auth page
- enter valid email
- fillin registration form
- submit data
- check your location - My Account

test_alert_invalid_data_create_account -
- open main page
- go to auth page
- enter existing email to creation form
- check alert error message

test_alert_invalid_data_login -
- open main page
- go to auth page
- enter invalid email to registration form
- check alert error message

test_add_delete_product_cart - 
- login to the store
- go to catalog
- open 'summer dresses' section
- add first product to cart
- proceed to checkout
- check main elements
- remove product
- check alert 


Problems:
- I couldn’t sort products by any parametrs (constant buffering + 403 (Forbidden) )
- potentially I can add product thru the search (just using hover + input_data methods from StoreBase.py and reuse the same checks in cart)
- no restrictions on password entry/validation (characters, no any security)
- no check in register form (e.g. accepts spaces)
- no history, with every new session the cart is updated



What need to improve:
- cover all asserts by raises
- not sure about elements checks (it's easier on mobile iOS/Android due to fewer items on the screen the same as on the mobile web; need to check main + cover visibility by smth like screen_tests >> based on transferring to page + .await some elements and then take a screenshot, you can go thru all flow manually + keep history of versions)
- Ruby is more familiar for me, but I haven't ever worked with it together with Selenium.
