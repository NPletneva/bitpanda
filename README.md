# test_task_bp
- all tests are in MyStoreTest.py - test’s scripts
- StoreBase.py - basic accessor methods for elements, contains methods common for all tests
- LoginFlowTestCase.py - contains methods/locators specific for login flow test
- AccountTestCase - contains methods/locators specific for account test
- CartTestCase - contains methods/locators specific for order cart tests
- CatalogTestCase - contains methods/locators specific for catalog tests
- all data are in common.yml
- ci.yml - configuration setup to run tests ci

- all testruns history are in 'Actions' tab here in GitHub.


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
- couldn’t sort products by any parametrs (constant buffering + 403 (Forbidden) )
- potentially there is an ability to add product thru the search (just using hover + input_data methods from StoreBase.py and reuse the same checks in cart)
- no restrictions on password entry/validation (characters, no any security)
- no check in register form (e.g. accepts spaces)
- no history, with every new session the cart is updated


What need to improve:
- cover all asserts by raises
