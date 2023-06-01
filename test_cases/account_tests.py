import os
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage
from pages.my_account_dashboard_page import DashboardPage
from pages.lost_password_page import LostPasswordPage
from pages.reset_password_sent_email_page import SentEmailPage


class TestAccount(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://skleptest.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_create_account(self):
        main_page = MainPage(self.driver)
        main_page.click_account_button()
        my_account_page = MyAccountPage(self.driver)
        my_account_page.type_in_reg_email('finalproject@finalproject.pl')
        my_account_page.type_in_reg_password('Finalproject1234')
        my_account_page.click_register_button()
        my_account_dashboard = DashboardPage(self.driver)
        my_account_dashboard.confirm_account_login()

    def test_logout(self):
        main_page = MainPage(self.driver)
        main_page.click_account_button()
        my_account_page = MyAccountPage(self.driver)
        my_account_page.type_in_username('finalproject@finalproject.pl')
        my_account_page.type_in_password('Finalproject1234')
        my_account_page.click_login_button()
        dashboard = DashboardPage(self.driver)
        dashboard.click_logout_button()
        dashboard.click_confirm_logout()
        main_page.title_of_page()

    def test_reset_password(self):
        main_page = MainPage(self.driver)
        main_page.click_account_button()
        my_account_page = MyAccountPage(self.driver)
        my_account_page.click_lost_your_password_button()
        lost_password_page = LostPasswordPage(self.driver)
        lost_password_page.type_in_username_or_email('finalproject@finalproject.pl')
        lost_password_page.click_reset_password_button()
        email_sent = SentEmailPage(self.driver)
        email_sent.sent_email_page_url()

    @classmethod
    def tearDown(self):
        self.driver.quit()