import csv

hospitals = gpd.read_file('game_grid_export/facilities/hospitals.shp')
small_hospitals = hospitals.loc[hospitals['BEDS'] < 200].to_crs(epsg=3857)
large_hospitals = hospitals.loc[hospitals['BEDS'] >= 200].to_crs(epsg=3857)
ems = gpd.read_file('game_grid_export/facilities/EMS.shp')
large_ems = ems.loc[ems['TOTAL_VEHI'] >= 5] 
small_ems = ems.loc[ems['TOTAL_VEHI'] < 5] 
shelters = gpd.read_file('game_grid_export/facilities/shelters.shp') 
fire_stations = gpd.read_file('game_grid_export/facilities/fire_stations.shp') 
local_eocs = gpd.read_file('game_grid_export/facilities/local_eocs.shp') 
state_eocs = gpd.read_file('game_grid_export/facilities/state_eocs.shp') 
cell_towers = gpd.read_file('game_grid_export/facilities/cell_towers.shp') 

with open('test.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['objectid', 'type', 'food_water', 'medicine', 'fuel'])

    for objectid in small_hospitals['ID']: 
        filewriter.writerow([objectid, 'hospital_s', 150, 150, 0])
    for objectid in large_hospitals['ID']:
        filewriter.writerow([objectid, 'hospital_l', 300, 300, 0])
    for objectid in large_ems['ID']:
        filewriter.writerow([objectid, 'ems_l', 0, 150, 0])
    for objectid in small_ems['ID']:
        filewriter.writerow([objectid, 'ems_s', 0, 75, 0])
    for objectid in shelters['ID']:
        filewriter.writerow([objectid, 'shelter', 300, 0, 0])
    for objectid in fire_stations['ID']:
        filewriter.writerow([objectid, 'fire_station', 0, 0, 0])
    for objectid in local_eocs['OBJECTID']:
        filewriter.writerow([objectid, 'eoc_local', 0, 0, 0])
    for objectid in state_eocs['OBJECTID']:
        filewriter.writerow([objectid, 'eoc_state', 0, 0, 0])
    for objectid in cell_towers['OBJECTID']:
        filewriter.writerow([objectid, 'cell_tower', 0, 0, 60])
