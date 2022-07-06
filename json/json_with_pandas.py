import json
import pandas as pd

filename = '/data1/tmp/vehicle_stops_2016_datasd_clean_json/part-00000-b7691d0c-2052-4892-887a-19bf1b29cf1e.json'
# filename = 'data/vehicle_stops.json'
data = []
with open(filename, 'r') as file:
    data.append(json.loads(file.readline()))
#
# print(data[0]['sd_resident'])

df = pd.DataFrame(data)
print(df.head())
