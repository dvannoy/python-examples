import requests
import json

r = requests.get('https://pkgstore.datahub.io/core/house-prices-us/cities_json/data/fdb183dfcd2ac5b1525f4b1ca2634880/cities_json.json')
data = r.json()
print(json.dumps(data, indent=2))
#for i in data:

