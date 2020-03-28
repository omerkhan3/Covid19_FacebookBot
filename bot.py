import logging
import json
import requests
from pprint import pprint

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class State:
    def __init__(self, state):
        self.state = state
        self.url = 'http://coronavirusapi.com/getTimeSeries/'

    def getStateData(self):
        url = self.url + self.state.upper()
        resp = requests.get(url)
        json = self.buildStateJSON(resp.text)
        return json

    def buildStateJSON(self, data):
        jsawn = {}
        jsawn[self.state] = data
        return json.dumps(jsawn)

class Country:
    def __init__(self):
        self.url = 'https://api.covid19api.com/'

    def getCountries(self):
        payload = {}
        headers = {}
        curl = self.url + "countries"
        countries = requests.request("GET", curl, headers=headers, data = payload)
        return countries.json()

    def getCurrentLive(self):
        payload = {}
        headers = {}
        countries = self.getCountries()
        confirmed = []
        for each in countries:
            curl = self.url + "country/" + each["Slug"] + "/status/confirmed"
            byCountry = requests.request("GET", curl, headers=headers, data = payload)
            confirmed.append(byCountry.text)
        return confirmed

    def getCountryTotals(self):
        payload = {}
        headers = {}
        countries = self.getCountries()
        totals = []
        for each in countries:
            curl = self.url + "total/country/" + each["Slug"] + "/status/confirmed"
            totalsByCountry = requests.request("GET", curl, headers=headers, data = payload)
            totals.append(totalsByCountry.text)
        return totals

def buildStates(states):
    """Simple function to iterate list argument to pull data"""
    stateData = []
    for state in states:
        state = State(state)
        data = state.getStateData()
        stateData.append(data)
    return stateData

def main():
    states = ['CO', 'MI', 'NY', 'CA']
    #stateData = buildStates(states)
    countryData = Country()
    #confirmed = countryData.getCurrentLive()
    totals = countryData.getCountryTotals()
    print(totals)

    #print(stateData)
main()

