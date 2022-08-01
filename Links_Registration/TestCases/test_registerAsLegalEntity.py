import random
import string
import pytest
from selenium import webdriver
from PageObjects.Links_RegistrationPage import Registration
from Utilities.readProperties import ReadConfig


class Test002RegisterAsLegalEntity:
    url = ReadConfig.get_url()
    companyName = ReadConfig.get_company_name()
    companyOIB = ReadConfig.get_company_oib()
    companyEmail = ReadConfig.get_company_email()
    companyContact = ReadConfig.get_company_contact()
    companyPerson = ReadConfig.get_company_contact()
    companyAddress = ReadConfig.get_company_address()
    companyCity = ReadConfig.get_company_city()
    companyPostalCode = ReadConfig.get_company_postalcode()

    def test_register_as_legal_entity(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.rgl = Registration(self.driver)
        self.rgl.clear_cookie()
        self.rgl.select_legal_entity()
        self.rgl.enter_company_name(self.companyName)
        self.rgl.enter_company_oib(self.companyOIB)
        self.rgl.enter_company_email(self.companyEmail)
        self.rgl.enter_company_contact(self.companyContact)
        self.rgl.enter_company_person(self.companyPerson)
        self.rgl.enter_company_address(self.companyAddress)
        self.rgl.enter_company_postalcode(self.companyPostalCode)
        self.rgl.enter_company_city(self.companyCity)
