import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo en un DataFrame de pandas
ruta_archivo = r'Analisis_HotSale\analisis hotsale 20203 - reporte_de_ventas (9).csv.csv'
df = pd.read_csv(ruta_archivo, sep=',')

# Convert the 'Imp. Total' column to a numeric data type
#df['Imp. Total'] = pd.to_numeric(df['Imp. Total'].str.replace('.', '').str.replace(',', '.'), errors='coerce')

# Remove outliers and store in a new DataFrame
df_no_outliers = df[np.abs(df['Imp. Total'] - df['Imp. Total'].mean()) <= (3 * df['Imp. Total'].std())]

# Visualize the distribution of the 'Imp. Total' column without outliers
sns.histplot(df_no_outliers['Imp. Total'], bins=20)
plt.show()
