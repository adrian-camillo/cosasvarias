import pandas as pd

# Ruta de acceso al archivo CSV
ruta_archivo = 'analisis retail\ReporteDeVentasDiciembre2022Hasta15Mayo2023.csv'

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(ruta_archivo)

# Eliminar las comillas dobles en los valores de la columna 'Nro Suc'
df['Nro Suc'] = df['Nro Suc'].str.strip('"')

# Definir el diccionario de coordenadas
coordenadas = {
    "18": (-32.84203712977546, -68.83373977491861),
    "11": (-29.41390832532731, -66.85654050390991),
    "17": (-31.41459387425563, -64.18328190382098),
    "3": (-31.413735630365473, -64.18470786149294),
    "21": (-28.470076887620326, -65.77843384627809),
    "7": (-31.41521750589497, -64.18351946149305),
    "22": (-27.73032369316184, -64.23828803281697),
    "26": (-31.396942090075065, -64.23546160382168),
    "15": (-31.396942090075065, -64.23546160382168),
    "20": (-27.784094891812924, -64.26181717390827),
    "12": (-29.4129253242431, -66.85661147507398),
    "1": (-31.415208349773078, -64.18348727498497),
    "23": (-28.470102215041788, -65.77846054427576)
}

# Agregar la columna 'Ubicación Coordenadas' con los valores correspondientes
df['Ubicación Coordenadas'] = df['Nro Suc'].map(coordenadas)

# Mostrar el DataFrame resultante
print(df)





import folium
from folium.plugins import MarkerCluster

# Filtrar los datos con 'Tarjeta Tipo' igual a "PREFER"
df_prefer = df[df['Tarjeta tipo'].str.contains('PREFER', na=False)]

# Crear el mapa centrado en Argentina
mapa = folium.Map(location=[-34.6037, -58.3816], zoom_start=4)

# Agregar los marcadores de coordenadas para cada registro
marker_cluster = MarkerCluster().add_to(mapa)
for _, row in df_prefer.iterrows():
    ubicacion = row['Ubicación Coordenadas']
    folium.Marker(ubicacion).add_to(marker_cluster)

# Mostrar el mapa
mapa.save('mapa_prefer.html')









# Filtrar los datos con 'Tarjeta Tipo' diferente a '-' y '---'
df_valores_diferentes = df[~df['Tarjeta tipo'].isin(['-', '---'])]

# Crear el mapa centrado en Argentina
mapa_valores_diferentes = folium.Map(location=[-34.6037, -58.3816], zoom_start=4)

# Agregar los marcadores de coordenadas para cada registro
marker_cluster_valores_diferentes = MarkerCluster().add_to(mapa_valores_diferentes)
for _, row in df_valores_diferentes.iterrows():
    ubicacion = row['Ubicación Coordenadas']
    folium.Marker(ubicacion).add_to(marker_cluster_valores_diferentes)

# Mostrar el mapa
mapa_valores_diferentes.save('mapa_valores_diferentes.html')
