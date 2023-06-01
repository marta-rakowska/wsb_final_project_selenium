from pages.base_page import BasePage


class CheckoutPage(BasePage):
    show_login_xpath = "//*[@class='showlogin']"
    username_xpath = "//*[@id='username']"
    password_xpath = "//*[@id='password']"
    login_xpath = "//*[@name='login']"
    first_name_xpath = "//*[@id='billing_first_name']"
    last_name_xpath = "//*[@id='billing_last_name']"
    street_xpath = "//*[@id='billing_address_1']"
    postcode_xpath = "//*[@id='billing_postcode']"
    city_xpath = "//*[@id='billing_city']"
    phone_xpath = "//*[@id='billing_phone']"
    email_address_xpath = "//*[@id='billing_email']"
    check_payments_xpath = "//*[@id='payment_method_cheque']"
    place_order_xpath = "//*[@id='place_order']"

    def click_show_login_button(self):
        self.wait_for_element_to_be_clickable(self.show_login_xpath)
        self.click_on_the_element(self.show_login_xpath)

    def click_login_button(self):
        self.wait_for_element_to_be_clickable(self.login_xpath)
        self.click_on_the_element(self.login_xpath)

    def type_in_username(self, username):
        self.wait_for_element_to_be_clickable(self.username_xpath)
        self.field_send_keys(self.username_xpath, username)

    def type_in_password(self, password):
        self.wait_for_element_to_be_visible(self.password_xpath)
        self.field_send_keys(self.password_xpath, password)

    def type_in_first_name(self, first_name):
        self.wait_for_element_to_be_clickable(self.first_name_xpath)
        self.field_send_keys(self.first_name_xpath, first_name)

    def type_in_last_name(self, last_name):
        self.field_send_keys(self.last_name_xpath, last_name)

    def type_in_street(self, street):
        self.field_send_keys(self.street_xpath, street)

    def type_in_postcode(self, postcode):
        self.field_send_keys(self.postcode_xpath, postcode)

    def type_in_city(self, city):
        self.field_send_keys(self.city_xpath, city)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_xpath, phone)

    def type_in_email(self, email):
        self.field_send_keys(self.email_address_xpath, email)

    def click_check_payments_button(self):
        self.wait_for_element_to_be_clickable(self.check_payments_xpath)
        self.click_on_the_element(self.check_payments_xpath)

    def click_place_order_button(self):
        self.wait_for_element_to_be_clickable(self.place_order_xpath)
        self.click_on_the_element(self.place_order_xpath)









