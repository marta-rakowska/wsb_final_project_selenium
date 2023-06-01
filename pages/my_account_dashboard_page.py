from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    logout_button_xpath = "//*[contains(text(),'Logout')]"
    confirm_logout_xpath = "//*[contains(text(),'Confirm')]"
    my_account_orders_xpath = "//*/nav/ul/li[2]/a"
    my_account_dashboard_xpath = "//*/nav/ul/li[1]/a"

    def click_logout_button(self):
        self.wait_for_element_to_be_clickable(self.logout_button_xpath)
        self.click_on_the_element(self.logout_button_xpath)

    def click_confirm_logout(self):
        self.wait_for_element_to_be_clickable(self.confirm_logout_xpath)
        self.click_on_the_element(self.confirm_logout_xpath)

    def confirm_account_login(self):
        self.wait_for_element_to_be_clickable(self.my_account_dashboard_xpath)
        assert self.driver.find_element(By.XPATH, self.my_account_orders_xpath).is_displayed()



