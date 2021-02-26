from LoginFlowTestCase import LoginFlowHelper
from MyAccountTestCase import MyAccountHelper
from CatalogTestCase import CatalogHelper
from CartTestCase import CartHelper


def test_create_account(browser):
    sign_in_page = LoginFlowHelper(browser)
    my_account_page = MyAccountHelper(browser)
    sign_in_page.open_sign_in_page()
    assert "Login - My Store" in browser.title
    sign_in_page.verify_lexemes_sign_in_page()
    sign_in_page.fill_in_email_to_create_account()
    sign_in_page.submit_button_to_create_account()
    sign_in_page.fill_in_registration_form()
    sign_in_page.submit_button_to_register()
    assert "My account - My Store" in browser.title
    assert 'controller=my-account' in browser.current_url
    my_account_page.verify_my_account_page("creation")


def test_alert_invalid_data_create_account(browser):
    sign_in_page = LoginFlowHelper(browser)
    sign_in_page.open_sign_in_page()
    assert "Login - My Store" in browser.title
    sign_in_page.fill_in_exist_email_to_create_account()
    sign_in_page.submit_button_to_create_account()
    sign_in_page.verify_invalid_data_alert_for_create_acc_form()


def test_alert_invalid_data_login(browser):
    sign_in_page = LoginFlowHelper(browser)
    sign_in_page.open_sign_in_page()
    assert "Login - My Store" in browser.title
    sign_in_page.fill_in_invalid_date_to_login()
    sign_in_page.submit_button_to_login()
    sign_in_page.verify_invalid_data_alert_for_login_form()


def test_add_delete_product_cart(browser):
    sign_in_page = LoginFlowHelper(browser)
    my_account_page = MyAccountHelper(browser)
    catalog_page = CatalogHelper(browser)
    cart_page = CartHelper(browser)
    sign_in_page.open_sign_in_page()
    assert "Login - My Store" in browser.title
    sign_in_page.verify_lexemes_sign_in_page()
    sign_in_page.fill_in_email_to_log_in()
    sign_in_page.fill_in_password_to_log_in()
    sign_in_page.submit_button_to_login()
    assert "My account - My Store" in browser.title
    assert 'controller=my-account' in browser.current_url
    my_account_page.verify_my_account_page("signin")
    catalog_page.open_summer_dresses_section()
    assert "Summer Dresses - My Store" in browser.title
    catalog_page.set_list_view()
    catalog_page.add_product_to_cart()
    catalog_page.proceed_to_checkout()
    assert "Order - My Store" in browser.title
    cart_page.verify_cart(1)
    cart_page.delete_product_from_cart()
    cart_page.verify_cart_empty()
