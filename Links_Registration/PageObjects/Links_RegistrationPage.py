import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Registration:
    """Legal entity objects:"""
    legalEntity_checkbox_id = "RegisterAsCompany"
    companyName_textbox_id = "Company"
    companyOIB_textbox_id = "CompanyOIB"
    companyEmail_textbox_id = "CompanyEmail"
    companyContact_textbox_id = "CompanyTelephone"
    companyPerson_texbox_id = "CompanyContactPerson"
    companyAddress_texbox_id = "CompanyAddress"
    companyPostalCode_texbox_xpath = "(//input[@class='ui-autocomplete-input'])[1]"
    companyCity_texbox_path = "(//input[@class='ui-autocomplete-input'])[2]"

    """Natural person objects:"""
    maleGender_radio_id = "gender-male"
    femaleGender_radio_id = "gender-female"
    firstname_textbox_id = "FirstName"
    lastname_textbox_id = "LastName"
    dobDay_dropdown_xpath = "//select[@name='DateOfBirthDay']"
    day_selection_xpath = "//*[text()='10']"
    month_selection_xpath = "//*[text()='rujan']"
    year_selection_xpath = "//*[text()='2022']"
    dobMonth_dropdown_xpath = "//select[@name='DateOfBirthMonth']"
    dobYear_dropdown_xpath = "//select[@name='DateOfBirthYear']"
    email_textbox_id = "Email"
    address_textbox_id = "StreetAddress"
    postcode_textbox_xpath = "(//input[@class='ui-autocomplete-input'])[3]"
    city_textbox_xpath = "(//input[@class='ui-autocomplete-input'])[4]"
    contact_textbox_id = "Phone"
    newsletter_textbox_id = "Newsletter"
    password_textbox_id = "Password"
    confirmpassword_textbox_id = "ConfirmPassword"
    register_button_id = "register-button"
    cookie_button_id = "eu-cookie-ok"

    """Validation message objects"""
    sameEmailValidation_text_xpath = "//div[@class='validation-summary-errors']"
    firstNameValidation_text_xpath = "//span[@data-valmsg-for='FirstName']"
    lastNameValidation_text_xpath = "//span[@data-valmsg-for='LastName']"
    invalidEmailVal_text_xpath = "//span[@data-valmsg-for='Email']"
    passwordValidation_text_xpath = "//span[@data-valmsg-for='Password']"
    confirmPasswordValidation_text_xpath = "//span[@data-valmsg-for='ConfirmPassword']"

    def __init__(self, driver):
        self.driver = driver

    """Legal entity methods"""
    def select_legal_entity(self):
        self.driver.find_element("id", self.legalEntity_checkbox_id).click()

    def enter_company_name(self, company_name):
        self.driver.find_element("id", self.companyName_textbox_id).send_keys(company_name)

    def enter_company_oib(self, company_oib):
        self.driver.find_element("id", self.companyOIB_textbox_id).send_keys(company_oib)

    def enter_company_email(self, company_email):
        self.driver.find_element("id", self.companyEmail_textbox_id).send_keys(company_email)

    def enter_company_contact(self, company_contact):
        self.driver.find_element("id", self.companyContact_textbox_id).send_keys(company_contact)

    def enter_company_person(self, company_person):
        self.driver.find_element("id", self.companyPerson_texbox_id).send_keys(company_person)

    def enter_company_address(self, company_address):
        self.driver.find_element("id", self.companyAddress_texbox_id).send_keys(company_address)

    def enter_company_postalcode(self, company_postalcode):
        self.driver.find_element("xpath", self.postcode_textbox_xpath).send_keys(company_postalcode)

    def enter_company_city(self, company_city):
        self.driver.find_element("xpath", self.companyCity_texbox_path).send_keys(company_city)

    """natural person methods"""

    def select_gender(self, gender):
        self.driver.find_element("id", self.femaleGender_radio_id).click()

    def enter_firstname(self, firstname):
        self.driver.find_element("id", self.firstname_textbox_id).clear()
        self.driver.find_element("id", self.firstname_textbox_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element("id", self.lastname_textbox_id).clear()
        self.driver.find_element("id", self.lastname_textbox_id).send_keys(lastname)

    def select_dob(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.day_selection_xpath)))
        self.driver.find_element("xpath", self.dobDay_dropdown_xpath).click()
        self.driver.find_element("xpath", self.day_selection_xpath).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.month_selection_xpath)))
        self.driver.find_element("xpath", self.dobMonth_dropdown_xpath).click()
        self.driver.find_element("xpath", self.month_selection_xpath).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.year_selection_xpath)))
        self.driver.find_element("xpath", self.dobYear_dropdown_xpath).click()
        self.driver.find_element("xpath", self.year_selection_xpath).click()

    def enter_email(self, email):
        self.driver.find_element("id", self.email_textbox_id).clear()
        self.driver.find_element("id", self.email_textbox_id).send_keys(email)

    def enter_address(self, address):
        self.driver.find_element("id", self.address_textbox_id).clear()
        self.driver.find_element("id", self.address_textbox_id).send_keys(address)

    def enter_postalcode(self, postalcode):
        self.driver.find_element("xpath", self.postcode_textbox_xpath).clear()
        self.driver.find_element("xpath", self.postcode_textbox_xpath).send_keys(postalcode)

    def enter_city(self, city):
        self.driver.find_element("xpath", self.city_textbox_xpath).clear()
        self.driver.find_element("xpath", self.city_textbox_xpath).send_keys(city)

    def enter_contact(self, contact):
        self.driver.find_element("id", self.contact_textbox_id).clear()
        self.driver.find_element("id", self.contact_textbox_id).send_keys(contact)

    def select_newsletter(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(("id", self.newsletter_textbox_id)))
        self.driver.find_element("id", self.newsletter_textbox_id).click()

    def set_password(self, password):
        self.driver.find_element("id", self.password_textbox_id).send_keys(password)

    def confirm_password(self, confirm_password):
        self.driver.find_element("id", self.confirmpassword_textbox_id).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element("id", self.register_button_id).click()

    def clear_cookie(self):
        self.driver.find_element("id", self.cookie_button_id).click()

    """Validation methods"""

    def same_email_validation(self):
        same_validation_message = self.driver.find_element("xpath", self.sameEmailValidation_text_xpath).text
        assert 'Navedena elektronska pošta/adresa postoji' in same_validation_message

    def first_name_validation(self):
        name_validation_message = self.driver.find_element("xpath", self.firstNameValidation_text_xpath).text
        assert "Ime je potrebno" in name_validation_message

    def last_name_validation(self):
        name_validation_message = self.driver.find_element("xpath", self.lastNameValidation_text_xpath).text
        assert "Prezime je potrebno" in name_validation_message

    def invalid_email_validation(self):
        invalid_email_validation_message = self.driver.find_element("xpath", self.invalidEmailVal_text_xpath).text
        assert "Elektronska pošta je potrebna" in invalid_email_validation_message

    def password_validation(self):
        password_validation = self.driver.find_element("xpath", self.passwordValidation_text_xpath).text
        assert "Lozinka je potrebna." in password_validation

    def confirm_password_validation(self):
        confirm_password_validation = self.driver.find_element("xpath", self.confirmPasswordValidation_text_xpath).text
        assert "Lozinka je potrebna." in confirm_password_validation
