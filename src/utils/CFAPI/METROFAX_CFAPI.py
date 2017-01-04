#!/usr/bin/env python

# CFAPI INTERFACE
import requests
import json


class RestAdapter(object):

    def __init__(self, base_url):
        self.base_url = base_url

    def get_regions_by_country_with_inventory(self, country_code):
        route = "/CFAPI/GetRegionsByCountryWithInventory/"
        call_route = requests.get(self.base_url + route + country_code)
        json_object = json.loads(call_route.content)
        return json_object

    def get_cities_by_state_with_inventory(self, country_code, state_code):
        route = "/Widget/GetCitiesByStateWithInventory/"
        call_route = requests.get(self.base_url + route +
                                  country_code + "/" + state_code)
        json_object = json.loads(call_route.content)
        return json_object

    def get_phone_numbers_with_inventory(self, num_code):
        route = "/Widget/GetPhoneNumbersWithInventory/"
        call_route = requests.get(self.base_url + route + num_code + "/null/1")
        json_object = json.loads(call_route.content)
        return json_object
