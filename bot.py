import logging
import json
import requests
from flask import Flask, request
from pprint import pprint
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import atexit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class StateData:
    def __init__(self):
        self.url = 'http://coronavirusapi.com/getTimeSeries/'
        self.stateList = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        self.stateData = {}
        self.buildStates()

    def getStateTotals(self):
        return self.stateData

    def constructStateData(self, state):
        url = self.url + state.upper()
        logger.info(url)
        resp = requests.get(url)
        clean = resp.text.split('\n')[-1]
        cleaner = clean.split(',')[2]
        logger.info(cleaner)
        return cleaner

    def buildStates(self):
        """Simple function to iterate list argument to pull data"""
        stateData = []
        for state in self.stateList:
            logger.info(state)
            data = self.constructStateData(state)
            self.stateData[state] = data

class CountryData:
    def __init__(self):
        self.url = 'https://api.covid19api.com/'
        self.countriesTotals = {}
        #self.countriesMapping = self.parseCountriesMapping(jsonFile)

    def getCountriesTotal(self):
        return self,countriesTotal

    def __call__(self):
        return self.countriesTotals

    def getCountriesMapping(self):
        return self.countriesMapping

    def parseCountriesMapping(self, jsonFile):
        return 0

    def getCountriesSummary(self):
        payload = {}
        headers = {}
        curl = self.url + "summary"
        logger.info(curl)
        countries = requests.request("GET", curl, headers=headers, data = payload)
        logger.info(countries.status_code)
        return countries.json()

    def getCountryTotals(self):
        payload = {}
        headers = {}
        countries = self.getCountriesSummary()
        for each in countries["Countries"]:
            logger.info(each)
            self.countriesTotals[each['Country']] = each
        return self.countriesTotals

countryData = CountryData()
stateData = StateData()

@app.route("/countryTotals", methods=['GET', 'POST'])
def getCountryData():
    global countryData
    logger.info(str(countryData.getCountryTotals()))
    return str(countryData.getCountryTotals())

@app.route("/stateTotals", methods=['GET', 'POST'])
def getStateData():
    global stateData
    logger.info(str(stateData.getStateTotals()))
    return str(stateData.getStateTotals())

# def main():
#     global countryData
#     #stateData = StateData()
#     #print (stateData.getStateData())
#     #countryData = CountryData()
#     totals = countryData.getCountryTotals()
#     print(totals)
#
# main()

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=getCountryData, trigger='interval', seconds=5)
    scheduler.add_job(func=getStateData, trigger='interval', seconds=6)
    scheduler.start()
    app.run(debug=True)

    atexit.register(lambda: scheduler.shutdowm())
