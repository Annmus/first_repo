from selenium import webdriver
import time
import datetime
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


def czekaj_na_id(element_id):
    timeout = 5
    timeout_message = f'Element o id {element_id} nie pojawil sie w czasie {timeout} s.'

    lokalizator = ('id', element_id) #szukanie po id konkretnej wartości
    znaleziono = excon.visibility_of_element_located(lokalizator) #patyk do dzgania strony
    #obiekt bedzie pytany, czy jest ok, a odpowiedz bedzie zalezelc od tego, czy element jest widoczny
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    driver.get_screenshot_as_file(screenshot)

opcje = webdriver.ChromeOptions()
opcje.add_argument('headless')

driver = webdriver.Chrome(options= opcje)
driver.get('https://www.saucedemo.com/')


try:
    login_button = czekaj_na_id('login-button')
except TimeoutException:
    print('nie znaleziono')
else:
    print('znaleziono')
finally:
    make_screenshot(driver)
    time.sleep(2)
    driver.quit()