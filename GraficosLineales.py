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





#Line graph of customer count over time, "Clientes Unicos" - Prefer vs No Prefer
plt.figure(figsize=(10,6))
df_grouped_by_date_una_compra_prefer = df_una_compra_prefer.groupby('Fecha')['DNI / CUIT'].nunique()
df_grouped_by_date_una_compra_no_prefer = df_una_compra_no_prefer.groupby('Fecha')['DNI / CUIT'].nunique()
plt.plot(df_grouped_by_date_una_compra_prefer.index, df_grouped_by_date_una_compra_prefer.values, label='"Clientes Únicos" - Prefer')
plt.plot(df_grouped_by_date_una_compra_no_prefer.index, df_grouped_by_date_una_compra_no_prefer.values, label='"Clientes Únicos" - No Prefer')
plt.title('Numero de clientes a traves del tiempo ("Clientes Únicos" - Prefer vs No Prefer)')
plt.xlabel('Fecha')
plt.ylabel('Conteo de clientes')
plt.legend()
plt.savefig('grafico16.png')
plt.close()

#Line graph of customer count over time, "Clientes Renovadores" vs "Clientes Únicos"
plt.figure(figsize=(10,6))
df_grouped_by_date_dos_compras = df_clientes_dos_compras.groupby('Fecha')['DNI / CUIT'].nunique()
df_grouped_by_date_una_compra = df_clientes_una_compra.groupby('Fecha')['DNI / CUIT'].nunique()
plt.plot(df_grouped_by_date_dos_compras.index, df_grouped_by_date_dos_compras.values, label='Clientes "Renovadores"')
plt.plot(df_grouped_by_date_una_compra.index, df_grouped_by_date_una_compra.values, label='Clientes "Únicos"')
plt.title('Numero de clientes a traves del tiempo (Comparison: "Clientes Renovadores" vs "Clientes Únicos")')
plt.xlabel('Fecha')
plt.ylabel('Conteo de clientes')
plt.legend()
plt.savefig('grafico15.png')
plt.close()

# Gráfico 7: Line graph of customer count over time, "Clientes Recurrentes" - Prefer vs No Prefer vs Mixto
plt.figure(figsize=(10,6))
df_grouped_by_date_dos_compras_prefer = df_dos_compras_prefer.groupby('Fecha')['DNI / CUIT'].nunique()
df_grouped_by_date_dos_compras_no_prefer = df_dos_compras_no_prefer.groupby('Fecha')['DNI / CUIT'].nunique()
df_grouped_by_date_clientes_mixto = df_clientes_dos_compras_mixto.groupby('Fecha')['DNI / CUIT'].nunique()
plt.plot(df_grouped_by_date_dos_compras_prefer.index, df_grouped_by_date_dos_compras_prefer.values, label='"Clientes Recurrentes" - Prefer')
plt.plot(df_grouped_by_date_dos_compras_no_prefer.index, df_grouped_by_date_dos_compras_no_prefer.values, label='"Clientes Recurrentes" - No Prefer')
plt.plot(df_grouped_by_date_clientes_mixto.index, df_grouped_by_date_clientes_mixto.values, label='"Clientes Recurrentes" - Mixto')
plt.title('Numero de clientes a traves del tiempo ("Clientes Recurrentes" - Prefer vs No Prefer vs Mixto)')
plt.xlabel('Fecha')
plt.ylabel('Conteo de clientes')
plt.legend()
plt.savefig('grafico14.png')
plt.close()

 #Gráfico 8: Line graph of customer count over time for all categories
plt.figure(figsize=(10,6))
df_counts = [df_combinado, df_clientes_dos_compras, df_dos_compras_prefer, df_dos_compras_no_prefer,
             df_clientes_dos_compras_mixto, df_clientes_una_compra, df_una_compra_prefer,
             df_una_compra_no_prefer, df_dos_compras_no_prefer_tarjeta, df_dos_compras_no_prefer_efectivo,
             df_dos_compras_no_prefer_mixto, df_una_compra_no_prefer_tarjeta, df_una_compra_no_prefer_efectivo]

labels = ['Combinado', 'Clientes con dos compras', 'Dos compras prefer', 'Dos compras no prefer',
          'Clientes dos compras mixto', 'Clientes con una compra', 'Una compra prefer',
          'Una compra no prefer', 'Dos compras no prefer tarjeta', 'Dos compras no prefer efectivo',
          'Dos compras no prefer mixto', 'Una compra no prefer tarjeta', 'Una compra no prefer efectivo']

for i, df_count in enumerate(df_counts):
    df_grouped_by_date = df_count.groupby('Fecha')['DNI / CUIT'].nunique()
    plt.plot(df_grouped_by_date.index, df_grouped_by_date.values, label=labels[i])

plt.title('Numero de clientes a traves del tiempo (comparacion de categorias)')
plt.xlabel('Fecha')
plt.ylabel('Conteo de clientes')
plt.legend()
plt.savefig('grafico13.png')
plt.close()















