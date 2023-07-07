import pandas as pd

ruta_archivo = r'C:/Users/adrian/Desktop/base de datos Nico-Calzados/Analisis_HotSale/analisis hotsale 20203 - reporte_de_ventas (9).csv.csv'

df = pd.read_csv(ruta_archivo, sep='\t', encoding='latin1', decimal=',', thousands='.', dtype={'Nro. Comp.': 'str', 'DNI / CUIT': 'str'})

# Drop any rows with missing data
df.dropna(inplace=True)

# Convert the 'Fecha' column to datetime format
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

# Remove the currency symbol and convert the 'Imp. Total' column to numeric format
df['Imp. Total'] = pd.to_numeric(df['Imp. Total'].str.replace('[$,]', ''), errors='coerce')

# Print the first 5 rows of the DataFrame
print(df.head())
