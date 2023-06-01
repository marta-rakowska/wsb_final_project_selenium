from pages.base_page import BasePage


class SearchResultPage(BasePage):
    magnolia_dress_xpath = "//*/header/div/div[2]/h2/a"
    search_results_expected_url = "https://skleptest.pl/?s=Magnolia+Dress"

    def search_result_page_url(self):
        self.wait_for_element_to_be_clickable(self.magnolia_dress_xpath)
        assert self.driver.current_url == self.search_results_expected_url