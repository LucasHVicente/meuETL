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
        assert len(obj.brazil_cases) == 27
        for item in obj.brazil_cases:
            assert item['uf'] in uf_list

    def test_export_brazil_to_csv(self):
        obj = CovidData()
        obj.export_brazil_to_csv()
        assert exists('brazil_covid_cases.csv')
        df = pd.read_csv('brazil_covid_cases.csv')
        assert len(df) == 27
    
    def test_export_brazil_to_csv_filter(self):
        obj = CovidData()
        obj.export_brazil_to_csv(states=['SP', 'RJ'])
        assert exists('brazil_covid_cases.csv')
        df = pd.read_csv('brazil_covid_cases.csv')
        assert len(df) == 2

    def test_export_world_to_csv(self):
        obj = CovidData()
        obj.export_world_to_csv()
        assert exists('world_covid_cases.csv')
        df = pd.read_csv('world_covid_cases.csv')
        assert len(df) == 199

    def test_export_world_to_csv(self):
        obj = CovidData()
        obj.export_world_to_csv(countries=['Brazil', 'Argentina'])
        assert exists('world_covid_cases.csv')
        df = pd.read_csv('world_covid_cases.csv')
        assert len(df) == 2