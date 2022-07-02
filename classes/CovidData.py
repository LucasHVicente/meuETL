import requests 
import pandas as pd
import json

class CovidData:
    def __init__(self, base_url = 'https://covid19-brazil-api.now.sh/api/report/v1/'):
        self.base_url = base_url
        self.brazillian_cases = []
    
    def fetch_cases(self):
        res = requests.get(self.base_url)
        self.brazillian_cases = json.loads(res.text)['data']

    def export_to_csv(self):
        df = pd.DataFrame(self.brazillian_cases)
        df.to_csv('brazil_covid_cases.csv', columns=['uf','state', 'cases', 'deaths', 'suspects', 'refuses', 'datetime'])