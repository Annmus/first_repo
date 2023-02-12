from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

pole_login = driver.find_element('id', 'user-name')

pole_haslo = driver.find_element('id', 'password')

pole_login.send_keys('standard_user')
pole_haslo.send_keys('secret_sauce')

button_login = driver.find_element('id', 'login-button')
button_login.submit()

driver.get_screenshot_as_file('screenshot.png')

time.sleep(10)