import logging
import json
import requests
from pprint import pprint

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)
#https://rapidapi.com/astsiatsko/api/coronavirus-monitor?endpoint=apiendpoint_17582575-ba9e-4539-b08e-6a7e24969470

class StateData:
    def __init__(self):
        self.url = 'http://coronavirusapi.com/getTimeSeries/'
        self.stateList = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        self.stateData = {}
        self.buildStates()

    def getStateData(self):
        return self.stateData

    def constructStateData(self, state):
        url = self.url + state.upper()
        resp = requests.get(url)
        clean = resp.text.split('\n')[-1]
        cleaner = clean.split(',')[2]
        return cleaner

    def buildStates(self):
        """Simple function to iterate list argument to pull data"""
        stateData = []
        for state in self.stateList:
            data = self.constructStateData(state)
            self.stateData[state] = data

class CountryData:
    def __init__(self):
        self.url = 'https://api.covid19api.com/'
        self.countriesTotals = {}
        #self.countriesMapping = self.parseCountriesMapping(jsonFile)

    def getCountriesTotal(self):
        return self,countriesTotal

    def getCountriesMapping(self):
        return self.countriesMapping

    def parseCountriesMapping(self, jsonFile):
        return 0

    def getCountriesSummary(self):
        payload = {}
        headers = {}
        curl = self.url + "summary"
        countries = requests.request("GET", curl, headers=headers, data = payload)
        return countries.json()

    def getCountryTotals(self):
        payload = {}
        headers = {}
        countries = self.getCountriesSummary()
        for each in countries["Countries"]:
            self.countriesTotals[each['Country']] = each
        return self.countriesTotals

def main():
    stateData = StateData()
    print (stateData.getStateData())
    countryData = CountryData()
    totals = countryData.getCountryTotals()
    print(totals)

main()
