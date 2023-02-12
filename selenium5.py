class LoginPage:
    def __int__(self, driver, user, passwd, login_button):
        self.driver = driver
        self.username_field = user
        self.password_field = passwd
        self.login_button = login_button

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


