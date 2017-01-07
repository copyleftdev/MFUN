from elements.FunnelELE import BasePageElement
from locators.FunnelLOC import FunnelLocs as Fl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select as Sel
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Factory
import random as rn
from datetime import date




class FunnelPageObjects(BasePageElement):

    def __init__(self, driver,base_url):
        self.base_url = base_url
        self.driver = driver
        self.f = Factory.create()
        self.wait = WebDriverWait(self.driver, 100)

    def buynow_funnel_signup(self, cn, sn=None, ptype=1):
        self.driver.get(self.base_url + "/buy-now/fax-numbers")
        country = self.driver.find_element(*Fl.COUNTRYDDL)
        state = self.driver.find_element(*Fl.STATEDDL)
        areacode = self.driver.find_element(*Fl.AREACODEDDL)

        #  Drop-Down Selection
        #  --------------------------------------------------------------------
        country_sel = Sel(country)
        state_sel = Sel(state)
        areacode_sel = Sel(areacode)

        country_sel.select_by_visible_text(cn)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                    "numberchooser-state")))
        if sn is None:
            state_count = state_sel.options
            state_sel.select_by_index(rn.randint(3, len(state_count) - 1))
        else:
            state_sel.select_by_visible_text(sn)

        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                    "numberchooser-city")))
        area_count = areacode_sel.options
        areacode_sel.select_by_index(rn.randint(3, len(area_count) - 1))
        # ----------------------------------------------------------------------
        # Conditionals for Plan Types
        # ----------------------------------------------------------------------
        if ptype == 1:  # Essential Monthly
            emonth = self.driver.find_element(*Fl.ESSENTIAL_MONTH_RDIO)
            self.wait.until(EC.element_to_be_clickable((By.ID,
                                                        "essential-month")))
            emonth.click()
            nextb = self.driver.find_element(*Fl.ESSENTIAL_NEXT_BTN)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                        "btnessential")))
        # ----------------------------------------------------------------------
        elif ptype == 2:  # Essential Annually
            eyear = self.driver.find_element(*Fl.ESSENTIAL_ANNUAL_RDIO)
            self.wait.until(EC.element_to_be_clickable((By.ID,
                                                        "essential-year")))
            eyear.click()
            nextb = self.driver.find_element(*Fl.ESSENTIAL_NEXT_BTN)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                        "btnessential")))
        # ----------------------------------------------------------------------
        elif ptype == 3:  # Value Monthly
            vmonth = self.driver.find_element(*Fl.VALUE_MONTH_RDIO)
            self.wait.until(EC.element_to_be_clickable((By.ID,
                                                        "value-month")))
            vmonth.click()
            nextb = self.driver.find_element(*Fl.VALUE_NEXT_BTN)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                        "btnvalue")))

        # ---------------------------------------------------------------------
        elif ptype == 4:  # Value Annually
            vyear = self.driver.find_element(*Fl.VALUE_ANNAUL_RDIO)
            self.wait.until(EC.element_to_be_clickable((By.ID,
                                                        "value-year")))
            vyear.click()
            nextb = self.driver.find_element(*Fl.VALUE_NEXT_BTN)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                        "btnvalue")))
        # ----------------------------------------------------------------------
        elif ptype == 5:  # Professional Monthly
            pmonth = self.driver.find_element(*Fl.PRO_MONTH_RDIO)
            self.wait.until(EC.element_to_be_clickable((By.ID,
                                                        "professional-month")))
            pmonth.click()
            nextb = self.driver.find_element(*Fl.PRO_NEXT_BTN)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                        "btnprofessional")))
        # ----------------------------------------------------------------------
        elif ptype == 6:  # Professional Annually
            pyear = self.driver.find_element(*Fl.PRO_ANNUAL_RDIO)
            self.wait.until(EC.element_to_be_clickable((By.ID,
                                                        "professional-year")))
            pyear.click()
            nextb = self.driver.find_element(*Fl.PRO_NEXT_BTN)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                        "btnprofessional")))
        else:
            return "{} invalid value for ptype".format(ptype)
        # ----------------------------------------------------------------------

        nextb.click()

    def populate_email_element(self):
        self.driver.get(self.base_url + "/buy-now/account-setup")
        email = self.driver.find_element(*Fl.EMAIL_INPT)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,
                                                        "email")))
        email.send_keys(self.f.company_email())
        next_btn = self.driver.find_element(*Fl.NEXT_STEP)
        self.wait.until(EC.presence_of_element_located((By.XPATH,
                        "//button[contains(text(),'NEXT STEP')]")))
        next_btn.click()




    def populate_billing_elements(self, cn, sn, ctype="visa16"):
        self.driver.get(self.base_url + "/Buy-Now/Billing-Info")
        fname = self.driver.find_element(*Fl.FNAME_INPT)
        lname = self.driver.find_element(*Fl.LNAME_INPT)
        company = self.driver.find_element(*Fl.COMPANY_NAME_INPT)
        address1 = self.driver.find_element(*Fl.ADDRESS_1_INPT)
        address2 = self.driver.find_element(*Fl.ADDRESS_2_INPT)
        city = self.driver.find_element(*Fl.BILL_CITY_INPT)
        zipcode = self.driver.find_element(*Fl.ZIPCODE_INPT)
        phonenum = self.driver.find_element(*Fl.PHONE_INPT)
        ccname = self.driver.find_element(*Fl.CARD_HOLDER_INPT)
        ccnum = self.driver.find_element(*Fl.CC_NUM_INPT)
        cvv = self.driver.find_element(*Fl.CVV_INPT)

        # Drop-Downs
        # ---------------------------------------------------------------------
        country = self.driver.find_element(*Fl.BILL_COUNTRY_DDL)
        country_sel = Sel(country)
        country_sel.select_by_visible_text(cn)

        state = self.driver.find_element(*Fl.BILL_STATE_DDL)
        state_sel = Sel(state)
        state_sel.select_by_visible_text(sn)

        ccmonth = self.driver.find_element(*Fl.MONTH_EXP_DDL)
        ccmonth_sel = Sel(ccmonth)
        ccmonth_sel.select_by_visible_text("06")

        ccyear = self.driver.find_element(*Fl.YEAR_EXP_DDL)
        ccyear_sel = Sel(ccyear)
        ccyear_sel.select_by_visible_text("{}".format(date.today().year + 2))

        card_type = self.driver.find_element(*Fl.CARD_TYPE_DDL)
        card_type_sel = Sel(card_type)
        card_type_sel.select_by_visible_text('VISA')

        # Using Faker to generate dynamic inputs
        # ----------------------------------------------------------------------
        fname.send_keys(self.f.first_name())
        lname.send_keys(self.f.last_name())
        company.send_keys(self.f.company())
        address1.send_keys(self.f.street_address())
        address2.send_keys(self.f.secondary_address())
        phonenum.send_keys(self.f.phone_number())
        ccname.send_keys(self.f.name())
        city.send_keys(self.f.city_suffix())
        zipcode.send_keys(self.f.zipcode())
        ccnum.send_keys("4133738662043055")
        cvv.send_keys("123")


    def assert_success_elements(self):
        pass
