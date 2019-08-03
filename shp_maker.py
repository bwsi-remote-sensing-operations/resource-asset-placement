# shapes = magic(0, 10000, flooding, 500, 0, 'hospital')['geometry']
# ^ Brian's magic function at work

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
geometry = shapes

data = {'objectid': objectid, 
        'type' : _type, 
        'geometry': geometry}

gdf = gpd.GeoDataFrame.from_dict(data)
gdf.crs = {'init' :'epsg:3857'}  
# project to merkator
gdf.to_crs({'init': 'epsg:3857'})
gdf.to_file('assets.shp')
