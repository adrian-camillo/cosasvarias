import pandas as pd
import glob
import geopandas as gpd
import matplotlib.pyplot as plt

path = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\creditos\archivosprocesados\HeatMap\archivosHeat'
all_files = glob.glob(path + "/*.csv")

li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

postales = pd.read_csv(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\creditos\archivosprocesados\HeatMap\AR.txt', delimiter="\t", header=None)
postales.columns = ['Country', 'PostalCode', 'Place', 'Province', 'A', 'Latitude', 'Longitude', 'D', 'Unknown1', 'Unknown2', 'Unknown3', 'Unknown4']

compras = frame.groupby('CODPOS').size().reset_index(name='Compras')
compras['CODPOS'] = compras['CODPOS'].astype(float)

merged = compras.merge(postales, left_on='CODPOS', right_on='PostalCode')

merged['Longitude'] = merged['Longitude'].fillna(merged['Unknown2'])
merged['Latitude'] = merged['Latitude'].fillna(merged['Unknown3'])

gdf = gpd.GeoDataFrame(
    merged, geometry=gpd.points_from_xy(merged.Latitude, merged.Longitude))
gdf.crs = "EPSG:4326"  # Establecer explícitamente el sistema de referencia de coordenadas

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

ax = world[world.name == 'Argentina'].plot(
    color='white', edgecolor='black')

gdf.plot(ax=ax, color='red')

plt.show()
