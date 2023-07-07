import pandas as pd
import numpy as np

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

# , 'Bancos'  es una columna que todavia no le asigne un dtype  

# Removing double quotes and converting monetary fields to float
money_columns = ['Imp. Total', 'Efectivo', 'Tarjetas', 'Cheq Terceros', 'Cuenta Corriente', 'Cheq Propios', 'Otras Cuentas']
print(df[money_columns])

df_procesado = df.copy()
print(df_procesado[money_columns])
import numpy as np
import pandas as pd

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

import locale
import re

# Configurar configuración regional
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

for col in money_columns:
    # Replace '-' with '0'
    df_procesado[col] = df_procesado[col].replace('-', '0')
    print(df_procesado[col])
    print(df_procesado[col].isnull().sum())

for col in money_columns:
    # Remove special characters ('$' and ',') and convert to numeric
    df_procesado[col] = df_procesado[col].str.replace('[$,]', '')
    df_procesado[col] = df_procesado[col].apply(lambda x: re.sub(r'[^0-9.]', '', x))
    df_procesado[col] = df_procesado[col].replace('', '0')
    df_procesado[col] = pd.to_numeric(df_procesado[col], errors='coerce')
    print(df_procesado[col].isnull().sum())
    print(df_procesado[col])

## SE PUEDEN REDONDEAR LOS ULTIMOS DOS DIGITOS QUE SERIAN LOS CENTAVOS PERO DA MAS PROBLEMAS QUE BENEFICIOS ASI QUE DE MOMENTO NO SE VA A HACER, YA SE PUEDE EXPORTAR
#### for col in money_columns:
    # Round the last two digits
    #df_procesado[col] = df_procesado[col].apply(lambda x: round(x, 3))
    #print(df_procesado[col])

print(df_procesado.dtypes)
print(df_procesado[money_columns])
print(df_procesado)
print(df)



# exporting de df_procesado
import pandas as pd

#df_procesado.to_csv('analisis retail/df_procesado.csv', index=False)




print(df_procesado)
#chequear tamaño de el df inicial y el df_procesado.csv