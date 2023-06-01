from pages.base_page import BasePage


class SentEmailPage(BasePage):
    email_sent_message_xpath = "//*[@class='woocommerce-message']"

    sent_email_expected_url = "https://skleptest.pl/my-account/lost-password/?reset-link-sent=true"

    def sent_email_page_url(self):
        self.wait_for_element_to_be_visible(self.email_sent_message_xpath)
        assert self.driver.current_url == self.sent_email_expected_url