from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class MainPage(BasePage):
    search_input_field_xpath = "//*[@id='search-field-top-bar']"
    account_button_xpath = "//*[contains(text(),'Account')]"
    site_description_xpath = "//*[@id='masthead']/div/div/div/div/p"
    cart_button_xpath = "//*[contains(text(),'My Cart')]"
    most_wanted_button_xpath = "//*[contains(text(),'Most')]"
    categories_button_xpath = "//*[@id='menu-item-123']"
    all_button_xpath = "//*[text()='All']"
    shirts_button_xpath = "//*[text()='Shirts']"
    featured_button_xpath = "//*[text()='Shirts']"
    trends_button_xpath = "//*[text()='Trends']"
    scarves_button_xpath = "//*[text()='Scarfs']"
    shoes_button_xpath = "//*[text()='Shoes']"
    tops_button_xpath = "//*[text()='Tops']"
    blouse_button_xpath = "//*[text()='Blouse']"
    jeans_button_xpath = "//*[text()='Jeans']"
    dresses_button_xpath = "//*[text()='Dresses']"
    newsletter_name_xpath = "//*[@id='es_txt_name']"
    newsletter_email_xpath = "//*[@id='es_txt_email']"
    newsletter_subscribe_xpath = "//*[@id='es_txt_button']"
    successfully_subscribed_xpath = "//*[@id='es_msg']"

    main_page_url = 'https://skleptest.pl/'
    expected_title = 'Generic Shop – Just another web shop'

    def click_account_button(self):
        self.wait_for_element_to_be_clickable(self.account_button_xpath)
        self.click_on_the_element(self.account_button_xpath)

    def click_search_input(self):
        self.wait_for_element_to_be_clickable(self.search_input_field_xpath)
        self.click_on_the_element(self.search_input_field_xpath)

    def type_in_search(self, search):
        self.field_send_keys(self.search_input_field_xpath, search)

    def press_enter(self):
        self.driver.find_element(By.ID, "search-field-top-bar").send_keys(Keys.ENTER)

    def title_of_page(self):
        self.wait_for_element_to_be_visible(self.site_description_xpath)
        assert self.get_page_title(self.main_page_url) == self.expected_title

    def type_in_newsletter_name(self, newsletter_name):
        self.field_send_keys(self.newsletter_name_xpath, newsletter_name)

    def type_in_newsletter_email(self, newsletter_email):
        self.field_send_keys(self.newsletter_email_xpath, newsletter_email)

    def click_subscribe_button(self):
        self.wait_for_element_to_be_clickable(self.newsletter_subscribe_xpath)
        self.click_on_the_element(self.newsletter_subscribe_xpath)

    def select_category(self, category):
        self.wait_for_element_to_be_clickable(self.categories_button_xpath)
        if category == 'All':
            self.wait_for_element_to_be_clickable(self.all_button_xpath)
            self.click_on_the_element(self.all_button_xpath)
        elif category == "Shirts":
            self.click_on_the_element(self.shirts_button_xpath)
        elif category == "Featured":
            self.click_on_the_element(self.featured_button_xpath)
        elif category == "Trends":
            self.click_on_the_element(self.trends_button_xpath)
        elif category == "Scarfs":
            self.click_on_the_element(self.scarves_button_xpath)
        elif category == "Shoes":
            self.click_on_the_element(self.shoes_button_xpath)
        elif category == "Tops":
            self.click_on_the_element(self.tops_button_xpath)
        elif category == "Blouse":
            self.click_on_the_element(self.blouse_button_xpath)
        elif category == "Jeans":
            self.click_on_the_element(self.jeans_button_xpath)
        else:
            self.click_on_the_element(self.dresses_button_xpath)

    def click_most_wanted_button(self):
        self.wait_for_element_to_be_clickable(self.most_wanted_button_xpath)
        self.click_on_the_element(self.most_wanted_button_xpath)

    def check_successful_subscription(self):
        self.wait_for_element_to_be_visible(self.successfully_subscribed_xpath)
        expected_text = "Successfully Subscribed."
        assert self.driver.find_element(By.XPATH, self.successfully_subscribed_xpath).text == expected_text

    def hover_over_categories(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH, "//*[@id='menu-item-123']")).perform()














