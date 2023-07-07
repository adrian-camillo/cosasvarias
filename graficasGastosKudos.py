import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('reporte_de_órdenes_de_pago (1).csv', sep=';')

df['Total'] = pd.to_numeric(df['Total'].str.replace('.', '').str.replace(',', '.'))
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
df.set_index('Fecha', inplace=True)

df.plot(kind='line', y='Total', legend=None)
plt.xlabel('Fecha')
plt.ylabel('Total')
plt.title('Total by Fecha')
plt.show()
