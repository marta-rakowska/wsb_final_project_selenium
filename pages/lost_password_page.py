from pages.base_page import BasePage


class LostPasswordPage(BasePage):
    username_or_email_xpath = "//*[@id='user_login']"
    reset_password_xpath = "//*/form/p[3]/input[2]"

    def type_in_username_or_email(self, email):
        self.wait_for_element_to_be_visible(self.username_or_email_xpath)
        self.field_send_keys(self.username_or_email_xpath, email)

    def click_reset_password_button(self):
        self.wait_for_element_to_be_clickable(self.reset_password_xpath)
        self.click_on_the_element(self.reset_password_xpath)



