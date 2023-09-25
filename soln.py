import pandas as pd

file_name = './cities.xlsx'
travel_df = pd.read_excel(file_name)
cities = travel_df.to_dict('records')

greenville = {'Area': 68, 'City': 'Greenville', 'Country': 'USA', 'Population': 84554}

greenville_population = greenville['Population']
greenville_area = greenville['Area']
city_keys = list(greenville) # alternative: city_keys = list(greenville.keys())

city_values = list(greenville.values())

salina = cities[-3]
los_cabos_pop = cities[3]['Population']
city_count = len(cities)
cities[11]['City'] = 'PyeongChang'

pyeongchang_values = list(cities[11].values())
pyeongchang_keys = list(cities[11].keys())
print(pyeongchang_keys)