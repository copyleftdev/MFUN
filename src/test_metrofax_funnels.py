import unittest
from selenium import webdriver
import pages.FunnelsPO as Fpo




class MetroFaxTestSuite(unittest.TestCase):



    def setUp(self):
        self.base_url = "https://qaorigin.metrofax.com"
        self.driver = webdriver.Firefox()
        self.workflow = Fpo.FunnelPageObjects(self.driver, self.base_url)
        self.driver.delete_all_cookies()


    def tearDown(self):
        pass

    @unittest.skip("Debug mode")
    def test_buy_now_funnel_signup(self):
        self.workflow.funnel_signup(cn='United States',
                                    sn="California", ptype=5,
                                    route="/buy-now/fax-numbers")
        self.workflow.populate_email_element("/buy-now/account-setup")
        self.workflow.populate_billing_elements("United States",
                                                "California",
                                                "/Buy-Now/Billing-Info")

    def test_free_trial_funnel_signup(self):
        self.workflow.funnel_signup(cn='United States',
                                    sn="California",
                                    route="/free-trial/fax-numbers")
        self.workflow.populate_email_element(route="/free-trial/account-setup")
        self.workflow.populate_billing_elements(cn="United States",
                                                sn="California",
                                                route="/free-trial/Billing-Info")

if __name__ == "__main__":
    unittest.main()
