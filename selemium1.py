from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
print('Nazw strony', driver.title)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
pole_szukaj = driver.find_element('name', 'q' )
pole_szukaj.send_keys('kicifura')
button2_szukaj = driver.find_element('name', 'btnK')
button2_szukaj.submit()
time.sleep(10)
