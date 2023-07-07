import pandas as pd
import matplotlib.pyplot as plt

# Leyendo los archivos csv
df1 = pd.read_csv('analisis retail\\ventas por marcas digital\\part1-000.csv', usecols=['groupingref', 'approvedorders'])
print(df1)
# Combinar los dos dataframes
df = pd.concat([df1])
print(df)
# Agrupar por marcas y sumar las ventas
df1 = df.groupby('groupingref').sum().sort_values(by='approvedorders', ascending=False)

# Seleccionar las primeras 15 marcas
df_top15 = df1.head(15)

# Crear el gráfico de barras
plt.figure(figsize=(10,6))
bars = plt.bar(df_top15.index, df_top15['approvedorders'])

# Colorear las primeras 10 barras en violeta y las siguientes 5 en cyan
for i in range(15):
    if i < 10:
        bars[i].set_color('violet')
    else:
        bars[i].set_color('cyan')

plt.xticks(rotation=90)  # Rotar los nombres de las marcas para mejor visualización
plt.title('15 marcas más vendidas')
plt.xlabel('Marcas')
plt.ylabel('Ventas')
plt.show()
