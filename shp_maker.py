import geopandas as gpd
from shapely.geometry import Polygon

generator_l = gpd.read_file('facilities/')

_type = []

for i in range(10):
    _type.append('generator_l')

for i in range(40):
    _type.append('cell_tower_mobile')



objectid = [i for i in range(1000001, 1000001 + len(_type))]
geometry = [Polygon([[0,0], [1,0], [1,1], [0,1]]),
            Polygon([[0,0], [1,0], [1,1], [0,1]]),
           ]

data = {'objectid': objectid, 
        'type' : _type, 
        'geometry': geometry}

print(len(_type))
print(len(objectid))
x = gpd.GeoDataFrame.from_dict(data)
print(x)

data.to_file('test.shp')
