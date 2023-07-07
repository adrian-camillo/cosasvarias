import pandas as pd
from datetime import datetime

# Lee el archivo CSV y lo carga en un DataFrame de Pandas
ruta_archivo = r'Analisis_HotSale\analisis hotsale 20203 - reporte_de_ventas (9).csv.csv'
df = pd.read_csv(ruta_archivo, sep=',')

# Convierte las fechas de string a datetime y crea una nueva columna 'Dia'
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
df['Dia'] = df['Fecha'].dt.date

# Convierte el campo 'Imp. Total' a un float y redondea los valores a dos decimales
df['Imp. Total'] = df['Imp. Total'].str.replace('$', '').str.replace(',', '').astype(float)
df['Imp. Total'] = df['Imp. Total'].apply(lambda x: round(x, 2))

# Reemplaza los valores faltantes por cero en 'Imp. Total'
df['Imp. Total'].fillna(0, inplace=True)

# Calcula el monto promedio de todas las compras
monto_promedio_total = df['Imp. Total'].mean()

# Calcula la moda de todas las compras si existen valores únicos
if df['Imp. Total'].nunique() > 0:
    monto_moda_total = df['Imp. Total'].mode().iloc[0]
else:
    monto_moda_total = 0

# Calcula la tendencia de todas las compras si hay más de un valor
if len(df['Imp. Total']) > 1:
    monto_tendencia_total = df['Imp. Total'].diff().mean(skipna=True)
else:
    monto_tendencia_total = 0

print(f'Monto promedio de todas las compras: ${monto_promedio_total:.2f}')
print(f'Monto moda de todas las compras: ${monto_moda_total:.2f}')
print(f'Tendencia de todas las compras: ${monto_tendencia_total:.2f}')

# Agrupa las compras por día y calcula el monto promedio y mediana de cada día
compras_por_dia = df.groupby('Dia')['Imp. Total'].agg(['mean', 'median'])

# Calcula la diferencia entre los montos promedio y mediana por día
compras_por_dia['Tendencia'] = compras_por_dia['mean'].diff()

print('\nMontos por día:')
print(compras_por_dia)
