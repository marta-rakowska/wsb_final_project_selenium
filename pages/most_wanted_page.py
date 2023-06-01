from pages.base_page import BasePage


class MostWantedPage(BasePage):
    rocadi_jeans_add_to_cart_xpath = "//*/div[2]/div/ul/li[3]/a[2]"
    magnolia_dress_add_to_cart_xpath = "//*/div[2]/div/ul/li[2]/a[2]"
    fitt_belts_add_to_cart_xpath = "//*/div[2]/div/ul/li[1]/a[2]"
    my_cart_button_xpath = "//*[contains(text(),'My Cart')]"

    def click_rocadi_jeans_cart_button(self):
        self.wait_for_element_to_be_clickable(self.rocadi_jeans_add_to_cart_xpath)
        self.click_on_the_element(self.rocadi_jeans_add_to_cart_xpath)

    def click_magnolia_dress_cart_button(self):
        self.wait_for_element_to_be_clickable(self.magnolia_dress_add_to_cart_xpath)
        self.click_on_the_element(self.magnolia_dress_add_to_cart_xpath)

    def click_fitt_belts_cart_button(self):
        self.wait_for_element_to_be_clickable(self.fitt_belts_add_to_cart_xpath)
        self.click_on_the_element(self.fitt_belts_add_to_cart_xpath)

    def click_my_cart_button(self):
        self.wait_for_element_to_be_clickable(self.my_cart_button_xpath)
        self.click_on_the_element(self.my_cart_button_xpath)