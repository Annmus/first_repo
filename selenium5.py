class LoginPage:
    def __init__(self, driver, user = 'user-name', passwd = 'password', login_button = 'login-button'):
        self.driver = driver
        self.username_field = user
        self.password_field = passwd
        self.login_button = login_button

    def open(self):
        self.driver.get('https://www.saucedemo.com/')

    def enter_username(self, username_data):
        field = self.driver.find_element('id', self.username_field)
        field.clear()
        field.send_keys(username_data)

    def enter_password(self, password_data):
        field = self.driver.find_element('id', self.password_field)
        field.clear()
        field.send_keys(password_data)

    def click_login_button(self):
        button = self.driver.find_element('id', self.login_button)
        button.click()


