#####################    IMPORTACION DE LIBRERIAS, FILTRADO Y CORRECCION DE DATOS        ##################

import pandas as pd

archivos = [
    'analisis retail/reporte_de_ventas_abril.csv',
    'analisis retail/reporte_de_ventas_diciembre_2022.csv',
    'analisis retail/reporte_de_ventas_enero.csv',
    'analisis retail/reporte_de_ventas_febrero.csv',
    'analisis retail/reporte_de_ventas_marzo.csv',
    'analisis retail/reporte_de_ventas_mayo_hasta_15.csv'
]

dataframes = []

for archivo in archivos:
    df = pd.read_csv(archivo, sep=';', encoding='latin-1', quoting=3)
    dataframes.append(df)

df_combinado = pd.concat(dataframes, ignore_index=True)

# Eliminar las comillas dobles de los nombres de las columnas
df_combinado.columns = df_combinado.columns.str.strip('"')

# Eliminar las comillas dobles de los valores en la columna "Fecha"
df_combinado['Fecha'] = df_combinado['Fecha'].str.strip('"')

# Convertir la columna "Fecha" al tipo de dato datetime
df_combinado['Fecha'] = pd.to_datetime(df_combinado['Fecha'], format='%d/%m/%Y')

# Ordenar el DataFrame por la columna "Fecha"
df_combinado = df_combinado.sort_values('Fecha')

df_combinado = df_combinado.reset_index(drop=True)

# Muestra del df final
print(df_combinado)

# Exportado a csv
#df_combinado.to_csv('ReporteDeVentasDiciembre2022Hasta15Mayo2023.csv', index=False)


#df solo para graficas de momento, prefer y no prefer pero en gral de la empresa ## 
# Filtrar las personas con 'PREFER' en la columna "Tarjeta tipo"
df_combinado_prefer = df_combinado[df_combinado['Tarjeta tipo'].str.contains('PREFER')]

# Filtrar las personas sin 'PREFER' y longitud total de caracteres >= 3
df_combinado_no_prefer = df_combinado[~df_combinado['Tarjeta tipo'].str.contains('PREFER') & (df_combinado['Tarjeta tipo'].str.len() >= 3)]



#########################                    CLIENTES QUE HAN COMPRADO MAS DE UNA VEZ             ####################333

# Paso 1: Agrupar por cliente y contar las compras
df_clientes_compras = df_combinado.groupby('Cliente').size().reset_index(name='NumCompras')

# Paso 2: Filtrar clientes con al menos dos compras
clientes_con_dos_compras = df_clientes_compras[df_clientes_compras['NumCompras'] >= 2]['Cliente']

# Paso 3: Filtrar el DataFrame original
df_clientes_dos_compras = df_combinado[df_combinado['Cliente'].isin(clientes_con_dos_compras)]

# Paso 4: Crear un nuevo DataFrame con los clientes seleccionados
df_clientes_dos_compras = df_clientes_dos_compras.reset_index(drop=True)

# Imprimir el nuevo DataFrame
print(df_clientes_dos_compras)

# Exportar a csv
#df_clientes_dos_compras.to_csv('ClientesRenovadores.csv', index=False)

# creacion de dataframe df_clientes_dos_compras_mixto (clientes que han comprado dos veces, al menos una con prefer)

# Paso 1: Filtrar clientes con al menos una compra con tarjeta tipo 'PREFER'
clientes_con_compra_prefer = df_clientes_dos_compras[df_clientes_dos_compras['Tarjeta tipo'].str.contains('PREFER', case=False)]['Cliente']

# Paso 2: Filtrar el DataFrame original
df_clientes_dos_compras_mixto = df_clientes_dos_compras[df_clientes_dos_compras['Cliente'].isin(clientes_con_compra_prefer)]

# Paso 3: Crear un nuevo DataFrame con los clientes seleccionados
df_clientes_dos_compras_mixto = df_clientes_dos_compras_mixto.reset_index(drop=True)

# Imprimir el nuevo DataFrame
print(df_clientes_dos_compras_mixto)

# Exportar a csv
df_clientes_dos_compras_mixto.to_csv('ClientesRenovadoresMixto.csv', index=False)

#############################################################33 CREACION DE DATAFRAMES PARA GRAFICOS ########################3333#############

import re

# Paso 1: Agrupar por cliente y contar las compras
df_clientes_compras = df_combinado.groupby('Cliente').size().reset_index(name='NumCompras')

# Paso 2: Filtrar clientes con solo una compra
clientes_con_una_compra = df_clientes_compras[df_clientes_compras['NumCompras'] == 1]['Cliente']

# Paso 3: Filtrar el DataFrame original
df_clientes_una_compra = df_combinado[df_combinado['Cliente'].isin(clientes_con_una_compra)]

# Paso 4: Crear un nuevo DataFrame con los clientes seleccionados
df_clientes_una_compra = df_clientes_una_compra.reset_index(drop=True)

# Imprimir el nuevo DataFrame
print("df_clientes_una_compra:")
print(df_clientes_una_compra)

# Exportar a CSV
#df_clientes_una_compra.to_csv('ClientesUnicaCompra.csv', index=False)

# Separar filas con 'PREFER' en la columna 'Tarjeta tipo' en df_clientes_dos_compras
df_dos_compras_prefer = df_clientes_dos_compras[df_clientes_dos_compras['Tarjeta tipo'].str.contains('PREFER')]

# Separar filas con 'PREFER' en la columna 'Tarjeta tipo' en df_clientes_una_compra
df_una_compra_prefer = df_clientes_una_compra[df_clientes_una_compra['Tarjeta tipo'].str.contains('PREFER')]

# Filtrar casos con 3 o más caracteres en la columna 'Tarjeta tipo' en df_dos_compras_prefer
df_dos_compras_prefer = df_dos_compras_prefer[df_dos_compras_prefer['Tarjeta tipo'].str.len() >= 3]

# Filtrar casos con 3 o más caracteres en la columna 'Tarjeta tipo' en df_una_compra_prefer
df_una_compra_prefer = df_una_compra_prefer[df_una_compra_prefer['Tarjeta tipo'].str.len() >= 3]

# Imprimir los nuevos DataFrames
print("df_clientes_dos_compras con 'PREFER' en Tarjeta tipo y 3 o más caracteres:")
print(df_dos_compras_prefer)

print("\ndf_clientes_una_compra con 'PREFER' en Tarjeta tipo y 3 o más caracteres:")
print(df_una_compra_prefer)


# Exportar a CSV
#df_dos_compras_prefer.to_csv('ClientesRenovadoresPREFER.csv', index=False)
#df_una_compra_prefer.to_csv('ClientesUnicaCompraPREFER.csv', index=False)

# Separar filas con medios de pago que no incluyan 'PREFER' y tengan más de un dígito en df_clientes_dos_compras
df_dos_compras_no_prefer = df_clientes_dos_compras[
    (~df_clientes_dos_compras['Tarjeta tipo'].str.contains('PREFER', na=False)) &
    (df_clientes_dos_compras['Tarjeta tipo'].str.contains(r'\d{2}', na=False))
]

# Separar filas con medios de pago que no incluyan 'PREFER' y tengan más de un dígito en df_clientes_una_compra
df_una_compra_no_prefer = df_clientes_una_compra[
    (~df_clientes_una_compra['Tarjeta tipo'].str.contains('PREFER', na=False)) &
    (df_clientes_una_compra['Tarjeta tipo'].str.contains(r'\d{2}', na=False))
]

# Imprimir los nuevos DataFrames
print("df_clientes_dos_compras sin 'PREFER' y con más de un dígito en Tarjeta tipo:")
print(df_dos_compras_no_prefer)

print("\ndf_clientes_una_compra sin 'PREFER' y con más de un dígito en Tarjeta tipo:")
print(df_una_compra_no_prefer)

# Exportar a CSV
#df_dos_compras_no_prefer.to_csv('ClientesRenovadoresNoPREFER.csv', index=False)
#df_una_compra_no_prefer.to_csv('ClientesUnicaCompraNoPREFER.csv', index=False)

# Creación de dataframes filtrados por tipo de pago y efectivo
df_dos_compras_no_prefer_tarjeta = df_dos_compras_no_prefer[df_dos_compras_no_prefer['Tarjeta tipo'] != '-']
df_dos_compras_no_prefer_efectivo = df_dos_compras_no_prefer[df_dos_compras_no_prefer['Efectivo'] != '0']
df_dos_compras_no_prefer_mixto = df_dos_compras_no_prefer[
    (df_dos_compras_no_prefer['Efectivo'] != '0') &
    (df_dos_compras_no_prefer['Tarjeta tipo'] != '-')
]

# Imprimir la longitud de los DataFrames filtrados
print("Longitud de df_dos_compras_no_prefer_tarjeta:", len(df_dos_compras_no_prefer_tarjeta))
print("Longitud de df_dos_compras_no_prefer_efectivo:", len(df_dos_compras_no_prefer_efectivo))
print("Longitud de df_dos_compras_no_prefer_mixto:", len(df_dos_compras_no_prefer_mixto))

# Exportar a CSV
#df_dos_compras_no_prefer_tarjeta.to_csv('df_dos_compras_no_prefer_tarjeta.csv', index=False)
#df_dos_compras_no_prefer_efectivo.to_csv('df_dos_compras_no_prefer_efectivo.csv', index=False)
#df_dos_compras_no_prefer_mixto.to_csv('df_dos_compras_no_prefer_mixto.csv', index=False)

# Creación de dataframes filtrados por tipo de pago y efectivo
df_una_compra_no_prefer_tarjeta = df_una_compra_no_prefer[df_una_compra_no_prefer['Tarjeta tipo'] != '-']
df_una_compra_no_prefer_efectivo = df_una_compra_no_prefer[df_una_compra_no_prefer['Efectivo'] != '0']
df_una_compra_no_prefer_mixto = df_una_compra_no_prefer[
    (df_una_compra_no_prefer['Efectivo'] != '0') &
    (df_una_compra_no_prefer['Tarjeta tipo'] != '-')
]

# Exportar a CSV
#df_una_compra_no_prefer_tarjeta.to_csv('df_una_compra_no_prefer_tarjeta.csv', index=False)
#df_una_compra_no_prefer_efectivo.to_csv('df_una_compra_no_prefer_efectivo.csv', index=False)
#df_una_compra_no_prefer_mixto.to_csv('df_una_compra_no_prefer_mixto.csv', index=False)

# Creación de dataframes filtrados por tipo de pago y efectivo
df_clientes_dos_compras_mixto_tarjeta = df_clientes_dos_compras_mixto[df_clientes_dos_compras_mixto['Tarjeta tipo'] != '-']
df_clientes_dos_compras_mixto_efectivo = df_clientes_dos_compras_mixto[df_clientes_dos_compras_mixto['Efectivo'] != '0']
df_clientes_dos_compras_mixto_mixto = df_clientes_dos_compras_mixto[
    (df_clientes_dos_compras_mixto['Efectivo'] != '0') &
    (df_una_compra_no_prefer['Tarjeta tipo'] != '-')
]
print("Longitud de df_clientes_dos_compras_mixto_tarjeta:", len(df_clientes_dos_compras_mixto_tarjeta))
print("Longitud de df_clientes_dos_compras_mixto_efectivo:", len(df_clientes_dos_compras_mixto_efectivo))
print("Longitud de df_clientes_dos_compras_mixto_mixto:", len(df_clientes_dos_compras_mixto_mixto))

#df_clientes_dos_compras_mixto_tarjeta.to_csv('df_dos_compras_no_prefer_tarjeta.csv', index=False)
#df_clientes_dos_compras_mixto_efectivo.to_csv('df_dos_compras_no_prefer_efectivo.csv', index=False)
#df_clientes_dos_compras_mixto_mixto.to_csv('df_dos_compras_no_prefer_mixto.csv', index=False)


#############################3                 GRAFICAS                                             ##############################3

import matplotlib.pyplot as plt

# Gráfico de torta: distribución cantidad de compras
labels_compras = ['Compras únicas', 'Compras múltiples']
sizes_compras = [len(df_clientes_una_compra), len(df_clientes_dos_compras)]
title_compras = 'Distribución cantidad de compras, diciembre 22 - Mayo 23'

plt.figure(figsize=(6, 6))
plt.pie(sizes_compras, labels=labels_compras, autopct='%1.1f%%', startangle=90)
plt.title(title_compras)
plt.axis('equal')
plt.show()

# Gráfico de torta: distribución clientes esporádicos
labels_esporadicos = ['Es prefer', 'No es prefer']
sizes_esporadicos = [len(df_una_compra_prefer), len(df_una_compra_no_prefer)]
title_esporadicos = 'Distribución clientes esporádicos'

plt.figure(figsize=(6, 6))
plt.pie(sizes_esporadicos, labels=labels_esporadicos, autopct='%1.1f%%', startangle=90)
plt.title(title_esporadicos)
plt.axis('equal')
plt.show()

# Gráfico de torta: distribución clientes recurrentes
labels_recurrentes = ['Es prefer', 'Mixto', 'No es prefer']
sizes_recurrentes = [len(df_dos_compras_prefer), len(df_clientes_dos_compras_mixto), len(df_dos_compras_no_prefer)]
title_recurrentes = 'Distribución clientes recurrentes'

plt.figure(figsize=(6, 6))
plt.pie(sizes_recurrentes, labels=labels_recurrentes, autopct='%1.1f%%', startangle=90)
plt.title(title_recurrentes)
plt.axis('equal')
plt.show()

# Gráfico de torta: distribución clientes recurrentes
labels_recurrentes = ['Es prefer', 'No es prefer']
sizes_recurrentes = [len(df_dos_compras_prefer), len(df_dos_compras_no_prefer)]
title_recurrentes = 'Distribución clientes recurrentes'

plt.figure(figsize=(6, 6))
plt.pie(sizes_recurrentes, labels=labels_recurrentes, autopct='%1.1f%%', startangle=90)
plt.title(title_recurrentes)
plt.axis('equal')
plt.show()



################# graficos que salen mal #################


# Gráfico de torta: distribución clientes esporádicos con crédito
labels_esporadicos_credito = ['Tarjeta', 'Efectivo', 'Mixto']
sizes_esporadicos_credito = [len(df_una_compra_no_prefer_tarjeta), len(df_una_compra_no_prefer_efectivo), len(df_una_compra_no_prefer_mixto)]
title_esporadicos_credito = 'Distribución clientes esporádicos con crédito'

plt.figure(figsize=(6, 6))
plt.pie(sizes_esporadicos_credito, labels=labels_esporadicos_credito, autopct='%1.1f%%', startangle=90)
plt.title(title_esporadicos_credito)
plt.axis('equal')
plt.show()

# Gráfico de torta: distribución clientes recurrentes sin crédito
labels_recurrentes_sin_credito = ['Tarjeta', 'Efectivo', 'Mixto']
sizes_recurrentes_sin_credito = [len(df_dos_compras_no_prefer_tarjeta), len(df_dos_compras_no_prefer_efectivo), len(df_dos_compras_no_prefer_mixto)]
title_recurrentes_sin_credito = 'Distribución clientes recurrentes sin crédito'

plt.figure(figsize=(6, 6))
plt.pie(sizes_recurrentes_sin_credito, labels=labels_recurrentes_sin_credito, autopct='%1.1f%%', startangle=90)
plt.title(title_recurrentes_sin_credito)
plt.axis('equal')
plt.show()

# Gráfico de torta: distribución clientes recurrentes con crédito >= 1
labels_recurrentes_con_credito = ['Tarjeta', 'Efectivo', 'Mixto']
sizes_recurrentes_con_credito = [len(df_clientes_dos_compras_mixto_tarjeta), len(df_clientes_dos_compras_mixto_efectivo), len(df_clientes_dos_compras_mixto_mixto)]
title_recurrentes_con_credito = 'Distribución clientes recurrentes con crédito >= 1'
#print test


plt.figure(figsize=(6, 6))
plt.pie(sizes_recurrentes_con_credito, labels=labels_recurrentes_con_credito, autopct='%1.1f%%', startangle=90)
plt.title(title_recurrentes_con_credito)
plt.axis('equal')
plt.show()



###########333 desde aca salen bien """"""""""""""


import matplotlib.pyplot as plt

# Obtener los tamaños de los DataFrames
size_prefer = len(df_combinado_prefer)
size_no_prefer = len(df_combinado_no_prefer)

# Configurar los datos y etiquetas para el gráfico
sizes = [size_prefer, size_no_prefer]
labels = ['Prefer', 'No Prefer']

# Configurar el título del gráfico
title = 'Distribución de Clientes: Prefer vs. No Prefer'

# Crear el gráfico de torta
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title(title)
plt.axis('equal')

# Mostrar el gráfico
plt.show()

#test
size_df_una_compra_no_prefer_tarjeta = len(df_una_compra_no_prefer_tarjeta)
print("Tamaño de df_una_compra_no_prefer_tarjeta:", size_df_una_compra_no_prefer_tarjeta)

size_df_dos_compras_no_prefer_efectivo = len(df_dos_compras_no_prefer_efectivo)
print("Tamaño de df_dos_compras_no_prefer_efectivo:", size_df_dos_compras_no_prefer_efectivo)

size_df_clientes_dos_compras_mixto_mixto = len(df_clientes_dos_compras_mixto_mixto)
print("Tamaño de df_clientes_dos_compras_mixto_mixto:", size_df_clientes_dos_compras_mixto_mixto)


size_df_una_compra_no_prefer_tarjeta = len(df_una_compra_no_prefer_tarjeta)
size_df_una_compra_no_prefer_efectivo = len(df_una_compra_no_prefer_efectivo)
size_df_una_compra_no_prefer_mixto = len(df_una_compra_no_prefer_mixto)

print("Tamaño de df_una_compra_no_prefer_tarjeta:", size_df_una_compra_no_prefer_tarjeta)
print("Tamaño de df_una_compra_no_prefer_efectivo:", size_df_una_compra_no_prefer_efectivo)
print("Tamaño de df_una_compra_no_prefer_mixto:", size_df_una_compra_no_prefer_mixto)


##############################3                DICTIONARY   incompleto                                          #############################3
# Crear un diccionario para almacenar información sobre la fuente de datos, FALTA DESARROLLO
info_dict = {
    'df_combinado': 'Datos combinados de varios archivos de ventas',
    'df_clientes_dos_compras': 'Clientes con más de una compra',
    'df_clientes_una_compra': 'Clientes con una única compra',
    'df_dos_compras_prefer': 'Clientes con más de una compra y tarjeta tipo PREFER',
    'df_una_compra_prefer': 'Clientes con una única compra y tarjeta tipo PREFER',
    'df_dos_compras_no_prefer': 'Clientes con más de una compra y tarjeta tipo distinta a PREFER y con más de un dígito',
    'df_una_compra_no_prefer': 'Clientes con una única compra y tarjeta tipo distinta a PREFER y con más de un dígito'
}

# Imprimir la información sobre la fuente de datos para cada DataFrame
for key, value in info_dict.items():
    print(key)
    print("Fuente de datos:", value)
    print()


    ################################3 TESTING ################33333
    # Imprimir la longitud de las columnas "tarjeta", "efectivo" y "mixto" en df_una_compra_no_prefer
print("Longitud de la columna 'tarjeta' en df_una_compra_no_prefer:", len(df_una_compra_no_prefer['tarjeta']))
print("Longitud de la columna 'efectivo' en df_una_compra_no_prefer:", len(df_una_compra_no_prefer['efectivo']))
print("Longitud de la columna 'mixto' en df_una_compra_no_prefer:", len(df_una_compra_no_prefer['mixto']))

# Imprimir la longitud de las columnas "tarjeta", "efectivo" y "mixto" en df_dos_compras_no_prefer
print("Longitud de la columna 'tarjeta' en df_dos_compras_no_prefer:", len(df_dos_compras_no_prefer['tarjeta']))
print("Longitud de la columna 'efectivo' en df_dos_compras_no_prefer:", len(df_dos_compras_no_prefer['efectivo']))
print("Longitud de la columna 'mixto' en df_dos_compras_no_prefer:", len(df_dos_compras_no_prefer['mixto']))

# Imprimir la longitud de las columnas "tarjeta", "efectivo" y "mixto" en df_clientes_dos_compras_mixto
print("Longitud de la columna 'tarjeta' en df_clientes_dos_compras_mixto:", len(df_clientes_dos_compras_mixto['tarjeta']))
print("Longitud de la columna 'efectivo' en df_clientes_dos_compras_mixto:", len(df_clientes_dos_compras_mixto['efectivo']))
print("Longitud de la columna 'mixto' en df_clientes_dos_compras_mixto:", len(df_clientes_dos_compras_mixto['mixto']))





labels_compras = ['Compras únicas', 'Compras múltiples']
sizes_compras = [len(df_clientes_una_compra), len(df_clientes_dos_compras)]
print(sizes_compras)



print("Columnas en df_una_compra_no_prefer:", df_una_compra_no_prefer.columns)
print("Column names in df_una_compra_no_prefer:", df_una_compra_no_prefer.columns)
print("Column names in df_dos_compras_no_prefer:", df_dos_compras_no_prefer.columns)
print("Column names in df_clientes_dos_compras_mixto:", df_clientes_dos_compras_mixto.columns)