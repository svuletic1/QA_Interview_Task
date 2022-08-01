import configparser
config = configparser.RawConfigParser()
# Set config path to match the path on your local machine
config_path = 'C:\\Users/stjep/PycharmProjects/Links_Registration/Configuration/config.ini'
config.read(config_path)

# Create methods to get data from confing.ini file
"""Natural person data methods"""


class ReadConfig:
    @staticmethod
    def get_url():
        url = config.get('Natural person data', 'url')
        return url

    @staticmethod
    def get_gender():
        gender = config.get('Natural person data', 'gender')
        return gender

    @staticmethod
    def get_firstname():
        firstname = config.get('Natural person data', 'firstname')
        return firstname

    @staticmethod
    def get_lastname():
        lastname = config.get('Natural person data', 'lastname')
        return lastname

    @staticmethod
    def get_email():
        email = config.get('Natural person data', 'email')
        return email

    @staticmethod
    def get_address():
        address = config.get('Natural person data', 'address')
        return address

    @staticmethod
    def get_postalcode():
        postalcode = config.get('Natural person data', 'postalcode')
        return postalcode

    @staticmethod
    def get_city():
        city = config.get('Natural person data', 'city')
        return city

    @staticmethod
    def get_contact():
        contact = config.get('Natural person data', 'contact')
        return contact

    @staticmethod
    def get_password():
        password = config.get('Natural person data', 'password')
        return password

    @staticmethod
    def get_confirm_password():
        confirm_password = config.get('Natural person data', 'confirmpassword')
        return confirm_password

    """Legal person data methods"""

    @staticmethod
    def get_company_name():
        company_name = config.get('Legal person data', 'companyname')
        return company_name

    @staticmethod
    def get_company_oib():
        company_oib = config.get('Legal person data', 'companyOIB')
        return company_oib

    @staticmethod
    def get_company_email():
        company_email = config.get('Legal person data', 'companyEmail')
        return company_email

    @staticmethod
    def get_company_contact():
        company_contact = config.get('Legal person data', 'companyContact')
        return company_contact

    @staticmethod
    def get_company_person():
        company_person = config.get('Legal person data', 'companyPerson')
        return company_person

    @staticmethod
    def get_company_address():
        company_address = config.get('Legal person data', 'companyAddress')
        return company_address

    @staticmethod
    def get_company_city():
        company_city = config.get('Legal person data', 'companyCity')
        return company_city

    @staticmethod
    def get_company_postalcode():
        company_postal_code = config.get('Legal person data', 'companyPostalCode')
        return company_postal_code

    """Mail Validation methods"""

    @staticmethod
    def get_mailinator_url():
        mailinator_url = config.get('Mailinator data', 'mailinator_url')
        return mailinator_url

    @staticmethod
    def get_email_prefix():
        email_prefix = config.get('Mailinator data', 'email_prefix')
        return email_prefix
