bro_man = magic(0, 10000, flooding, 500, 0, 'hospital')['geometry']

import geopandas as gpd
from shapely.geometry import Polygon

_type = []

for i in range(10):
    _type.append('generator_l')

for i in range(10):
    _type.append('cell_tower_mobile')

for i in range(19):
    _type.append('sandbag')
    
objectid = [i for i in range(1000001, 1000001 + len(_type))]
geometry = []



# just testing
for i in bro_man:
    geometry.append(i)

data = {'objectid': objectid, 
        'type' : _type, 
        'geometry': geometry}

bruh = gpd.GeoDataFrame.from_dict(data)

bruh.crs = {'init' :'epsg:3857'}  
# ^ comment out to get a "Cannot transform naive geometries" error below

# project to merkator
bruh.to_crs({'init': 'epsg:3857'})

bruh.to_file('assets.shp')
