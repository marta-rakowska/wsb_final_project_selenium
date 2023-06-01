import os
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.all_categories_page import AllCategoriesPage


class TestMainPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://skleptest.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_newsletter_subscription(self):
        main_page = MainPage(self.driver)
        main_page.type_in_newsletter_name('Python')
        main_page.type_in_newsletter_email('finalproject@finalproject.pl')
        main_page.click_subscribe_button()
        main_page.check_successful_subscription()

    def test_search(self):
        main_page = MainPage(self.driver)
        main_page.click_search_input()
        main_page.type_in_search('Magnolia Dress')
        main_page.press_enter()
        search_result_page = SearchResultPage(self.driver)
        search_result_page.search_result_page_url()

    def test_show_all_categories(self):
        main_page = MainPage(self.driver)
        main_page.hover_over_categories()
        main_page.select_category("All")
        all_categories = AllCategoriesPage(self.driver)
        all_categories.all_categories_page_url()

    @classmethod
    def tearDown(self):
        self.driver.quit()