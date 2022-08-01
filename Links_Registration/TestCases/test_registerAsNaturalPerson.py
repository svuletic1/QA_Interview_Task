import random
import string
import pytest
from selenium import webdriver
from PageObjects.Links_RegistrationPage import Registration
from Utilities.readProperties import ReadConfig


class Test001RegisterAsNaturalEntity:
    url = ReadConfig.get_url()

    # Natural person data
    gender = ReadConfig.get_gender()
    firstname = ReadConfig.get_firstname()
    lastname = ReadConfig.get_lastname()

    # comment email(line below(18)) if random email is wanted
    email = ReadConfig.get_email()
    address = ReadConfig.get_address()
    postalcode = ReadConfig.get_postalcode()
    city = ReadConfig.get_city()
    contact = ReadConfig.get_contact()
    password = ReadConfig.get_password()
    confirmpassword = ReadConfig.get_confirm_password()

    def test_register_as_natural_person(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.rg = Registration(self.driver)
        self.rg.clear_cookie()
        self.rg.select_gender(self.gender)
        self.rg.enter_firstname(self.firstname)
        self.rg.enter_lastname(self.lastname)
        self.rg.select_dob()

        """If random email address is wanted - uncomment random_generator method(bottom of the file)"""
        # self.email = random_generator() + '@mailinator.com'
        # self.rg.enterEmail(self.email)

        self.rg.enter_email(self.email)
        self.rg.enter_address(self.address)
        self.rg.enter_postalcode(self.postalcode)
        self.rg.enter_city(self.city)
        self.rg.enter_contact(self.contact)
        self.rg.select_newsletter()
        self.rg.set_password(self.password)
        self.rg.confirm_password(self.confirmpassword)
        self.rg.click_register()
        self.rg.same_email_validation()

        """Enter random email address every time"""
        # def random_generator(size=7, chars=string.ascii_lowercase + string.digits):
        #     return ''.join(random.choice(chars) for x in range(size))
