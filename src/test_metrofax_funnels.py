import unittest
from selenium import webdriver
import pages.FunnelsPO as Fpo
import rollbar



class MetroFaxTestSuite(unittest.TestCase):

    rollbar.init('0ee232063e624252aac3621bee9d3b01')

    def setUp(self):
        self.base_url = "https://qaorigin.metrofax.com"
        self.driver = webdriver.Firefox()
        self.workflow = Fpo.FunnelPageObjects(self.driver, self.base_url)
        self.driver.delete_all_cookies()


    def tearDown(self):
        self.driver.quit()

    def test_buy_now_funnel_signup(self):
        self.workflow.buynow_funnel_signup(cn='United States', ptype=2)
        self.workflow.populate_email_element()
        self.workflow.populate_billing_elements("United States", "California")

if __name__ == "__main__":
    unittest.main()
