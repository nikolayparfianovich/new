class login():

    def __init__(self,driver):
        self.driver=driver

        self.email_textbox_id="login-form-email"
        self.password_box_id="login-form-password"
        self.login_button_xpath="//button/span[text()='Login']"

    def enter_email(self,email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_box_id).clear()
        self.driver.find_element_by_id(self.password_box_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()


