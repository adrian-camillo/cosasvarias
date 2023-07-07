import pandas as pd
import numpy as np
import re

# Reading the csv
df = pd.read_csv(r'analisis retail\ReporteDeVentasDiciembre2022Hasta15Mayo2023.csv')

# Initial data visualization
print(df.head())
print(df)

# Null values check
print(df.isnull().sum())

# Dropping unnecessary columns
df.drop(columns=['¿Anulado?', 'Cliente', 'Lista de Precios', 'Otras F.Pago'], inplace=True)
print(df)

# Data types conversion
df['Nro Suc'] = df['Nro Suc'].apply(lambda x: pd.to_numeric(x.replace('"', '')) if pd.notnull(x) else np.nan)
df['Fecha'] = pd.to_datetime(df['Fecha'])
print(df)

# Columns requiring modification
money_columns = ['Imp. Total', 'Efectivo', 'Tarjetas', 'Cheq Terceros', 'Cuenta Corriente', 'Cheq Propios', 'Otras Cuentas']

df_procesado = df.copy()
print(df_procesado[money_columns])

for col in money_columns:
    # Convert the columns to string before applying the regular expression
    df_procesado[col] = df_procesado[col].astype(str)
    print(df_procesado[col])
    print(df_procesado[col].isnull().sum())

for col in money_columns:
    # Replaces the rows containing '-$' with 0
    df_procesado[col] = df_procesado[col].replace(r'.*-\$.*', '0', regex=True)
    print(df_procesado[col])
    print(df_procesado[col].isnull().sum())

# Remove special characters ('$' and ',') and convert to numeric
for col in money_columns:
    df_procesado[col] = df_procesado[col].str.replace('[$,]', '')
    df_procesado[col] = df_procesado[col].apply(lambda x: re.sub(r'[^0-9.]', '', x))
    df_procesado[col] = df_procesado[col].replace('', '0')
    df_procesado[col] = pd.to_numeric(df_procesado[col], errors='coerce')
    print(df_procesado[col].isnull().sum())
    print(df_procesado[col])

for col in money_columns:
    # Round the last two digits
    df_procesado[col] = df_procesado[col].apply(lambda x: round(x, 3))

    # Convert the columns to string before removing the last two digits
    df_procesado[col] = df_procesado[col].astype(str)
    df_procesado[col] = df_procesado[col].apply(lambda x: x[:-2])

    # Convert the columns back to numeric
    df_procesado[col] = pd.to_numeric(df_procesado[col], errors='coerce')
    print(df_procesado[col])

print(df_procesado.dtypes)
print(df_procesado[money_columns])
print(df_procesado)
print(df)
