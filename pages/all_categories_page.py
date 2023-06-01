from pages.base_page import BasePage


class AllCategoriesPage(BasePage):
    page_url = "https://skleptest.pl/shop/"
    all_page_header_xpath = "//*/div/div[2]/div/h1"

    def all_categories_page_url(self):
        self.wait_for_element_to_be_visible(self.all_page_header_xpath)
        assert self.driver.current_url == self.page_url
