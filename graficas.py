#chequear tamaño de el df inicial y el df_procesado.csv
import pandas as pd
import matplotlib.pyplot as plt
import re

# Load the data
df = pd.read_csv(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\analisis retail\Trabajables\df_procesado.csv')
print(df)

# Convert 'Fecha' to datetime type if it's not already
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['PREFER'] = df['Tarjeta tipo'].apply(lambda x: bool(re.search('PREFER', x)))
print(df)



###############3 intento raro : import pandas as pd

# df_combinado
df_combinado = df

# df_clientes_dos_compras
df_clientes_dos_compras = df[df.duplicated(['DNI / CUIT'], keep=False)]

# df_dos_compras_prefer
df_dos_compras_prefer = df_clientes_dos_compras[df_clientes_dos_compras['Tarjeta tipo'].str.contains('PREFER', na=False)]

# df_dos_compras_no_prefer
df_dos_compras_no_prefer = df_clientes_dos_compras[~df_clientes_dos_compras['Tarjeta tipo'].str.contains('PREFER', na=False)]

# df_clientes_dos_compras_mixto
df_clientes_dos_compras_mixto = df_clientes_dos_compras[df_clientes_dos_compras['DNI / CUIT'].isin(df_dos_compras_no_prefer['DNI / CUIT'])]

# df_clientes_una_compra
df_clientes_una_compra = df.drop_duplicates('DNI / CUIT', keep=False)

# df_una_compra_prefer
df_una_compra_prefer = df_clientes_una_compra[df_clientes_una_compra['Tarjeta tipo'].str.contains('PREFER', na=False)]

# df_una_compra_no_prefer
df_una_compra_no_prefer = df_clientes_una_compra[~df_clientes_una_compra['Tarjeta tipo'].str.contains('PREFER', na=False)]

# df_dos_compras_no_prefer_tarjeta
df_dos_compras_no_prefer_tarjeta = df_dos_compras_no_prefer[df_dos_compras_no_prefer['Tarjetas'] > 0]

# df_dos_compras_no_prefer_efectivo
df_dos_compras_no_prefer_efectivo = df_dos_compras_no_prefer[df_dos_compras_no_prefer['Efectivo'] > 0]

# df_dos_compras_no_prefer_mixto
df_dos_compras_no_prefer_mixto = df_dos_compras_no_prefer[(df_dos_compras_no_prefer['Tarjetas'] > 0) & (df_dos_compras_no_prefer['Efectivo'] > 0)]

# df_una_compra_no_prefer_tarjeta
df_una_compra_no_prefer_tarjeta = df_una_compra_no_prefer[df_una_compra_no_prefer['Tarjetas'] > 0]

# df_una_compra_no_prefer_efectivo
df_una_compra_no_prefer_efectivo = df_una_compra_no_prefer[df_una_compra_no_prefer['Efectivo'] > 0]


##############3333 GRAFICOS #####################

# Line graph of 'Imp. Total' over time
plt.figure(figsize=(10,6))
df_grouped_by_date = df.groupby('Fecha')['Imp. Total'].sum()
plt.plot(df_grouped_by_date.index, df_grouped_by_date.values)
plt.title('Total Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.savefig('grafico1.png')
plt.close()


# Filtrar los datos sin los canales 'CATALOGO' y 'ML FULL'
df_sin_catalogo_ml = df[~df['Canal'].isin(['"CATALOGO"', '"ML FULL"'])]

# Pie chart of 'Canal' sin los canales 'CATALOGO' y 'ML FULL'
plt.figure(figsize=(10,6))
df_canal = df_sin_catalogo_ml['Canal'].value_counts()
plt.pie(df_canal.values, labels=df_canal.index, autopct='%1.1f%%')
plt.title('Distribucion de canales (sin "CATALOGO" y  "ML FULL")')
plt.savefig('grafico2.png')
plt.close()


import matplotlib.pyplot as plt

# Obtener el número de clientes en cada DataFrame
num_clientes_dos_compras = df_clientes_dos_compras.shape[0]
num_clientes_una_compra = df_clientes_una_compra.shape[0]

# Los valores para cada sección
sizes = [num_clientes_dos_compras, num_clientes_una_compra]

# Las etiquetas para cada sección
labels = ['Clientes "Renovadores"', 'Clientes "Unicos"']

# Crear el gráfico de torta
plt.figure(figsize=(10,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Asegurarse de que el gráfico se muestra como un círculo
plt.axis('equal')

# Mostrar el gráfico
plt.savefig('grafico3.png')
plt.close()


# Gráfico 1: Comparación de clientes con dos compras y clientes con una compra
plt.figure(figsize=(6,6))
plt.pie([len(df_clientes_dos_compras), len(df_clientes_una_compra)], 
        labels=['Clientes "Renovadores"', 'Clientes "Unicos"'], 
        autopct='%1.1f%%')
plt.title('¿Cuantas compras han hecho nuestros clientes?')
plt.savefig('grafico4.png')
plt.close()

# Gráfico 2: Comparación de clientes con una compra no prefer (tarjeta) y clientes con una compra no prefer (efectivo)
plt.figure(figsize=(6,6))
plt.pie([len(df_una_compra_no_prefer_tarjeta), len(df_una_compra_no_prefer_efectivo)], 
        labels=['Tarjeta', 'Efectivo'], 
        autopct='%1.1f%%')
plt.title('Distribucion de metodo de pago "Clientes Unicos"')
plt.savefig('grafico5.png')
plt.close()
# Gráfico 3: Comparación de clientes con dos compras no prefer (tarjeta), clientes con dos compras no prefer (efectivo) y clientes con dos compras no prefer (mixto)
plt.figure(figsize=(6,6))
plt.pie([len(df_dos_compras_no_prefer_tarjeta), len(df_dos_compras_no_prefer_efectivo), len(df_dos_compras_no_prefer_mixto)], 
        labels=['Tarjeta', 'Efectivo', 'Mixto'], 
        autopct='%1.1f%%')
plt.title('Distribucion de metodo de pago "Clientes Recurrentes"')
plt.savefig('grafico6.png')
plt.close()

# Gráfico 4: Comparación de clientes con una compra prefer y clientes con una compra no prefer
plt.figure(figsize=(6,6))
plt.pie([len(df_una_compra_prefer), len(df_una_compra_no_prefer)], 
        labels=['Prefer', 'No Prefer'], 
        autopct='%1.1f%%')
plt.title('"Clientes Unicos": Prefer vs No Prefer')
plt.savefig('grafico7.png')
plt.close()

# Gráfico 5: Comparación de clientes con dos compras prefer y clientes con dos compras no prefer
plt.figure(figsize=(6,6))
plt.pie([len(df_dos_compras_prefer), len(df_dos_compras_no_prefer)], 
        labels=['Prefer', 'No Prefer'], 
        autopct='%1.1f%%')
plt.title('"Clientes Recurrentes": Prefer vs No Prefer')
plt.savefig('grafico7.png')
plt.close()

# Gráfico 6: Comparación de clientes con dos compras mixto, clientes con dos compras prefer y clientes con dos compras no prefer
plt.figure(figsize=(6,6))
plt.pie([len(df_clientes_dos_compras_mixto), len(df_dos_compras_prefer), len(df_dos_compras_no_prefer)], 
        labels=['"Clientes Recurrentes" mixto', '"Clientes Recurrentes" prefer', '"Clientes Recurrentes" no prefer'], 
        autopct='%1.1f%%')
plt.title('"Clientes Recurrentes": Prefer vs No Prefer vs Mixto')
plt.savefig('grafico8.png')
plt.close()

# Gráfico 7: Comparación de todas las categorías
plt.figure(figsize=(6,6))
plt.pie([len(df) for df in [df_combinado, df_clientes_dos_compras, df_dos_compras_prefer, df_dos_compras_no_prefer,
                            df_clientes_dos_compras_mixto, df_clientes_una_compra, df_una_compra_prefer,
                            df_una_compra_no_prefer, df_dos_compras_no_prefer_tarjeta, df_dos_compras_no_prefer_efectivo,
                            df_dos_compras_no_prefer_mixto, df_una_compra_no_prefer_tarjeta, df_una_compra_no_prefer_efectivo]], 
        labels=['Combinado', 'Clientes con dos compras', 'Dos compras prefer', 'Dos compras no prefer',
                'Clientes dos compras mixto', 'Clientes con una compra', 'Una compra prefer',
                'Una compra no prefer', 'Dos compras no prefer tarjeta', 'Dos compras no prefer efectivo',
                'Dos compras no prefer mixto', 'Una compra no prefer tarjeta', 'Una compra no prefer efectivo'], 
        autopct='%1.1f%%')
plt.title('Comparación de todas las categorías')
plt.savefig('grafico9.png')
plt.close()


# Grafico 8: Crear un DataFrame con el conteo de compras por canal y tarjeta tipo
import matplotlib.pyplot as plt

# Crear un DataFrame con el conteo de compras por canal y tarjeta tipo
##df_counts = df.groupby(['Canal', 'Tarjeta tipo']).size().unstack()

# Graficar las barras apiladas
##ax = df_counts.plot(kind='bar', stacked=True, figsize=(16, 16))

# Ocultar los nombres de las tarjetas en el eje x
##ax.set_xticklabels(df_counts.index, rotation=0)

##plt.title('Distribución de compras por Canal y Tarjeta tipo')
##plt.xlabel('Canal')
##plt.ylabel('Cantidad de Compras')
##plt.legend(title='Tarjeta tipo')
##plt.show()

# GraficoFiltrar el DataFrame por tarjeta tipo prefer y no prefer
df_prefer = df[df['Tarjeta tipo'].str.contains('PREFER', na=False)]
df_no_prefer = df[~df['Tarjeta tipo'].str.contains('PREFER', na=False)]

# Crear una lista de los datos de 'Imp. Total' para cada tarjeta tipo
data = [df_prefer['Imp. Total'], df_no_prefer['Imp. Total']]

# Graficar el diagrama de caja y bigotes
plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=['Prefer', 'No Prefer'])
plt.title('Distribución de Imp. Total por Tarjeta tipo')
plt.xlabel('Tarjeta tipo')
plt.ylabel('Imp. Total')
plt.savefig('grafico9.png')
plt.close()





#analisis :
# Importamos las librerías necesarias
import pandas as pd

# Asumimos que 'df' es tu DataFrame

# Cambiamos el tipo de dato de 'DNI / CUIT' a str para evitar problemas
df['DNI / CUIT'] = df['DNI / CUIT'].astype(str)

# Agrupamos por 'DNI / CUIT', contamos las frecuencias y sumamos el valor total
rfm_table = df.groupby('DNI / CUIT').agg({'Imp. Total': 'sum', 
                                          'DNI / CUIT': 'count'})

# Renombramos las columnas
rfm_table.rename(columns={'Imp. Total': 'Monetary', 
                          'DNI / CUIT': 'Frequency'}, inplace=True)

# Dividimos los datos en cuartiles para la segmentación
quantiles = rfm_table.quantile(q=[0.25,0.5,0.75])
quantiles = quantiles.to_dict()

# Creamos la segmentación
def RScore(x,p,d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]: 
        return 3
    else:
        return 4

rfm_table['f_quartile'] = rfm_table['Frequency'].apply(RScore, args=('Frequency',quantiles,))
rfm_table['m_quartile'] = rfm_table['Monetary'].apply(RScore, args=('Monetary',quantiles,))

print(rfm_table)



# Calculamos la matriz de correlación
correlation_matrix = df.corr()

# Imprimimos la matriz de correlación
print(correlation_matrix)

rfm_table_sorted = rfm_table.sort_values('Frequency', ascending=False)
print(rfm_table_sorted)
rfm_table_sorted.to_csv('C:\\Users\\adrian\\Desktop\\base de datos Nico-Calzados\\analisis retail\\rfm_table_sorted.csv')