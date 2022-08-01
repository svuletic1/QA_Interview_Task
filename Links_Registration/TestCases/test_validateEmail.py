import random
import string
import time
import pytest
from selenium import webdriver
from PageObjects.MailinatorPage import MailinatorPage
from Utilities.readProperties import ReadConfig


class Test004ValidateEmail:
    url1 = ReadConfig.get_mailinator_url()
    email_prefix = ReadConfig.get_email_prefix()

    def test_validate_email(self, setup):
        self.driver = setup
        self.driver.get(self.url1)
        self.driver.maximize_window()
        self.val1 = MailinatorPage(self.driver)
        self.val1.click_public_inbox()
        self.val1.enter_email_prefix(self.email_prefix)
        self.val1.click_go_button()
        time.sleep(2)
        self.val1.click_registration_mail()
        time.sleep(2)
        self.val1.click_links_tab()
        self.val1.click_registration_link()
        time.sleep(5)
