from elements.FunnelELE import BasePageElement as Bpe
from locators.FunnelLOC import FunnelLocs as Dl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select as Sel
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from utils.faker import Factory



class FunnelPageObjects(Bpe):

    def __init__(self, driver):
        self.driver = driver
        self.f = Faker.create()
        self.w = wait(self.driver, 10)

    def populate_fax_numbers_elements(self):
        pass

    def populate_email_element(self):
        pass

    def populate_billing_elements(self):
        pass

    def assert_success_elements(self):
        pass
