from classes.CovidData import CovidData

obj = CovidData()

obj.fetch_cases()
print(obj.brazillian_cases[0])
obj.export_to_csv()

