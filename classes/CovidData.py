import requests 
import pandas as pd
import json

class CovidData:
    def __init__(self):
        self.base_url = 'https://covid19-brazil-api.now.sh/api/report/v1/'
        self.brazil_cases = []
        self.world_cases = []
        self.fetch_cases()
    
    def fetch_cases(self):
        res = requests.get(self.base_url)
        self.brazil_cases = json.loads(res.text)['data']
        res = requests.get(self.base_url+'countries/')
        self.world_cases = json.loads(res.text)['data']

    def export_brazil_to_csv(self, columns=None, states=None):
        df = pd.DataFrame(self.brazil_cases)
        if states:
            df = df[df['uf'].isin(states)]
        df.to_csv('brazil_covid_cases.csv', columns=columns)

    def export_world_to_csv(self, columns=None, countries=None):
        df = pd.DataFrame(self.world_cases)
        if countries:
            df = df[df['country'].isin(countries)]
        df.to_csv('world_covid_cases.csv', columns=columns)