#####################    IMPORTACION DE LIBRERIAS, FILTRADO Y CORRECCION DE DATOS        ##################

import pandas as pd

archivos = [
    'analisis retail/reporte_de_ventas_abril.csv',
    'analisis retail/reporte_de_ventas_diciembre_2022.csv',
    'analisis retail/reporte_de_ventas_enero.csv',
]

dataframes = []

for archivo in archivos:
    df = pd.read_csv(archivo, sep=';', encoding='latin-1', quoting=3)
    dataframes.append(df)

df_combinado = pd.concat(dataframes, ignore_index=True)