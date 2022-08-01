import random
import string
import pytest
from selenium import webdriver
from PageObjects.Links_RegistrationPage import Registration
from Utilities.readProperties import ReadConfig


class Test003VerifyAllValidations:
    url = ReadConfig.get_url()

    def test_validations(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.val = Registration(self.driver)
        self.val.click_register()
        self.val.first_name_validation()
        self.val.last_name_validation()
        self.val.invalid_email_validation()
        self.val.password_validation()
        self.val.confirm_password_validation()
