from os.path import exists

import pandas as pd
from classes.CovidData import CovidData

uf_list = ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF']

class TestCovidData:
    def test_class_declared(self):
        obj = CovidData()
        assert isinstance(obj, CovidData)
    
    def test_fetch_cases(self):
        obj = CovidData()
        obj.fetch_cases()
        assert len(obj.brazilian_cases) == 27
        for item in obj.brazilian_cases:
            assert item['uf'] in uf_list

    def test_export_to_csv(self):
        obj = CovidData()
        obj.fetch_cases()
        obj.export_to_csv()
        assert exists('brazil_covid_cases.csv')
        df = pd.read_csv('brazil_covid_cases.csv')
        assert len(df) == 27

