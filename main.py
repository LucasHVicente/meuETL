from classes.CovidData import CovidData

obj = CovidData()

obj.export_brazil_to_csv(columns=['uf','state', 'cases', 'deaths', 'suspects', 'refuses', 'datetime'])

obj.export_brazil_to_csv(states=['SP', 'RJ'])

obj.export_world_to_csv()

obj.export_world_to_csv(countries=['Brazil', 'Argentina'])