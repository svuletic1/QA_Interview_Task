import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MailinatorPage:
    publicInbox_button_xpath = "//a[@class='inbox-link']"
    inbox_search_id = "inbox_field"
    go_button_xpath = "//button[@class='primary-btn']"
    registration_email_id = "row_svtest123-1659362832-229929156"
    links_tab_button_id = "pills-links-tab"
    registration_link_xpath = "(//a[@target='_other'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_public_inbox(self):
        self.driver.find_element("xpath", self.publicInbox_button_xpath).click()

    def enter_email_prefix(self, email_prefix):
        self.driver.find_element("id", self.inbox_search_id).send_keys(email_prefix)

    def click_go_button(self):
        self.driver.find_element("xpath", self.go_button_xpath).click()

    def click_registration_mail(self):
        self.driver.find_element("id", self.registration_email_id).click()

    def click_links_tab(self):
        self.driver.find_element("id", self.links_tab_button_id).click()

    def click_registration_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.registration_link_xpath))).click()
