from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderReceivedPage(BasePage):

    order_received = "//*/div[1]/div/header/h1"
    order_details = "//*/div/section[1]/h2"

    def check_order_received(self):
        self.wait_for_element_to_be_visible(self.order_received)
        assert self.driver.find_element(By.XPATH, self.order_details ).is_displayed()