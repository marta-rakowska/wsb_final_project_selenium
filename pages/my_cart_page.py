from pages.base_page import BasePage


class MyCartPage(BasePage):
    proceed_to_checkout_xpath = "//*[contains(text(),'Proceed')]"

    def click_proceed_to_checkout_button(self):
        self.wait_for_element_to_be_clickable(self.proceed_to_checkout_xpath)
        self.click_on_the_element(self.proceed_to_checkout_xpath)