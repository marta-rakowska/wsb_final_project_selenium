from pages.base_page import BasePage


class MyAccountPage(BasePage):
    reg_email_input_xpath = "//*[@id='reg_email']"
    reg_password_input_xpath = "//*[@id='reg_password']"
    register_button_xpath = "//*[@name='register']"
    lost_your_password_xpath = "//*[contains(text(),'Lost')]"
    username_input_xpath = "//*[@id='username']"
    password_input_xpath = "//*[@id='password']"
    login_button_xpath = "//*[@name='login']"

    def type_in_reg_email(self, reg_email):
        self.wait_for_element_to_be_visible(self.reg_email_input_xpath)
        self.field_send_keys(self.reg_email_input_xpath, reg_email)

    def type_in_reg_password(self, reg_password):
        self.wait_for_element_to_be_visible(self.reg_password_input_xpath)
        self.field_send_keys(self.reg_password_input_xpath, reg_password)

    def click_register_button(self):
        self.click_on_the_element(self.register_button_xpath)

    def click_lost_your_password_button(self):
        self.wait_for_element_to_be_clickable(self.lost_your_password_xpath)
        self.click_on_the_element(self.lost_your_password_xpath)

    def type_in_username(self, username):
        self.wait_for_element_to_be_visible(self.username_input_xpath)
        self.field_send_keys(self.username_input_xpath, username)

    def type_in_password(self, password):
        self.wait_for_element_to_be_visible(self.password_input_xpath)
        self.field_send_keys(self.password_input_xpath, password)

    def click_login_button(self):
        self.click_on_the_element(self.login_button_xpath)