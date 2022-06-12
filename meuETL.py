import requests 
import pandas as pd
import json

res = requests.get('https://covid19-brazil-api.now.sh/api/report/v1')
res_json = json.loads(res.text)

df = pd.DataFrame(res_json['data'])
df.to_csv('brazilian_states_covid_cases.csv')