import os
import unittest
import time

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.main_page import MainPage
from pages.most_wanted_page import MostWantedPage
from pages.my_cart_page import MyCartPage
from pages.checkout_page import CheckoutPage
from pages.order_received_page import OrderReceivedPage


class TestBuyWithoutCreatingAccount(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://skleptest.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_buy_as_returning_customer(self):
        main_page = MainPage(self.driver)
        main_page.click_most_wanted_button()
        most_wanted = MostWantedPage(self.driver)
        most_wanted.click_fitt_belts_cart_button()
        most_wanted.click_magnolia_dress_cart_button()
        most_wanted.click_rocadi_jeans_cart_button()
        most_wanted.click_my_cart_button()
        my_cart = MyCartPage(self.driver)
        my_cart.click_proceed_to_checkout_button()
        checkout = CheckoutPage(self.driver)
        checkout.type_in_first_name('Selenium')
        checkout.type_in_last_name('Webdriver')
        checkout.type_in_street('Testowa 1')
        checkout.type_in_postcode('11-111')
        checkout.type_in_city('WSB')
        checkout.type_in_phone('987654321')
        checkout.type_in_email('selenium@webdriver.pl')
        checkout.click_check_payments_button()
        checkout.click_place_order_button()
        order_received = OrderReceivedPage(self.driver)
        order_received.check_order_received()
        time.sleep(1)

    @classmethod
    def tearDown(self):
        self.driver.quit()