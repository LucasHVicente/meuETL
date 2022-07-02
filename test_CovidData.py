from os.path import exists
from classes.CovidData import CovidData

uf_list = ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF']

class TestCovidData:
    def test_class_declared(self):
        obj = CovidData()
        assert isinstance(obj, CovidData)
    
    def test_fetch_cases(self):
        obj = CovidData()
        obj.fetch_cases()
        assert len(obj.brazillian_cases) == 27
        for item in obj.brazillian_cases:
            assert item['uf'] in uf_list

    def test_export_to_csv(self):
        obj = CovidData()
        obj.fetch_cases()
        obj.export_to_csv()
        assert exists('brazil_covid_cases.csv')

