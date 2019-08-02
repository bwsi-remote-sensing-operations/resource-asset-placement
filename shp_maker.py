import geopandas as gpd

generator_l = gpd.read_file('facilities/')

_type = []

for i in range(10):
    _type.append('generator_l')

for i in range(40):
    _type.append('cell_tower_mobile')

for i in range(200):
    _type.append('sandbag')

objectid = [i for i in range(1000001, 1000001 + len(_type))]
geometry = [i for i in range(1000001, 1000001 + len(_type))]

data = {'objectid': objectid, 
        'type' : _type, 
        'geometry': geometry}

print(len(_type))
print(len(objectid))
x = gpd.GeoDataFrame.from_dict(data)
print(x)
