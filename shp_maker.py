import geopandas as gpd
from shapely.geometry import Polygon

_type = []

for i in range(10):
    _type.append('generator_l')

for i in range(40):
    _type.append('cell_tower_mobile')

for i in range(200):
    _type.append('sandbag')
objectid = [i for i in range(1000001, 1000001 + len(_type))]
geometry = []

for i in range(250):
    geometry.append(Polygon([[0,0], [1,0], [1,1], [0,1]]))

data = {'objectid': objectid, 
        'type' : _type, 
        'geometry': geometry}

x = gpd.GeoDataFrame.from_dict(data)

x.to_file('test.shp')
