import time
from selenium import webdriver
from selenium5 import LoginPage
import pytest

@pytest.mark.parametrize('uzytkownik, password, url', [('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
                                                       ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
                                                       ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
                                                       ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')])

def test_login_page(uzytkownik, password, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(uzytkownik)
    page.enter_password(password)
    page.click_login_button()
    time.sleep(2)
    try:
        assert driver.current_url == url
    finally:
        driver.quit()
