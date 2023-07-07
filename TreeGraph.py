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
print(df_clientes_dos_compras_mixto)
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
import pandas as pd
import matplotlib.pyplot as plt
import re
import plotly.graph_objects as go

# Load the data
df = pd.read_csv(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\analisis retail\Trabajables\df_procesado.csv')
print(df)

# Convert 'Fecha' to datetime type if it's not already
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['PREFER'] = df['Tarjeta tipo'].apply(lambda x: bool(re.search('PREFER', x)))
print(df)

# Data processing steps...

# Cuenta el número de clientes en cada categoría
num_total = df_combinado.shape[0]
num_una_compra = df_clientes_una_compra.shape[0]
num_una_compra_prefer = df_una_compra_prefer.shape[0]
num_una_compra_no_prefer = df_una_compra_no_prefer.shape[0]
num_una_compra_no_prefer_tarjeta = df_una_compra_no_prefer_tarjeta.shape[0]
num_una_compra_no_prefer_efectivo = df_una_compra_no_prefer_efectivo.shape[0]
num_una_compra_no_prefer_mixto = df_una_compra_no_prefer[(df_una_compra_no_prefer['Tarjetas'] > 0) & (df_una_compra_no_prefer['Efectivo'] > 0)].shape[0]
num_dos_compras = df_clientes_dos_compras.shape[0]
num_dos_compras_prefer = df_dos_compras_prefer.shape[0]
num_dos_compras_no_prefer = df_dos_compras_no_prefer.shape[0]
num_dos_compras_no_prefer_tarjeta = df_dos_compras_no_prefer_tarjeta.shape[0]
num_dos_compras_no_prefer_efectivo = df_dos_compras_no_prefer_efectivo.shape[0]
num_dos_compras_no_prefer_mixto = df_dos_compras_no_prefer[(df_dos_compras_no_prefer['Tarjetas'] > 0) & (df_dos_compras_no_prefer['Efectivo'] > 0)].shape[0]

labels = ["Total de clientes", "Clientes con una compra", "Clientes con una compra PREFER",
          "Clientes con una compra No PREFER", "Clientes con una compra No PREFER Tarjeta",
          "Clientes con una compra No PREFER Efectivo", "Clientes con una compra No PREFER Mixto", "Clientes con dos compras",
          "Clientes con dos compras PREFER", "Clientes con dos compras No PREFER",
          "Clientes con dos compras No PREFER Tarjeta", "Clientes con dos compras No PREFER Efectivo",
          "Clientes con dos compras No PREFER Mixto"]

colors = ['blue' if 'PREFER' not in label else 'red' for label in labels]

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=colors
    ),
    link=dict(
        source=[0, 0, 1, 1, 3, 3, 3, 0, 0, 6, 6, 8, 8, 8],  # Indices correspond to the 'labels' list
        target=[1, 7, 2, 3, 4, 5, 6, 8, 7, 9, 10, 11, 12],
        value=[num_una_compra, num_dos_compras, num_una_compra_prefer, num_una_compra_no_prefer,
               num_una_compra_no_prefer_tarjeta, num_una_compra_no_prefer_efectivo, num_una_compra_no_prefer_mixto,
               num_dos_compras_prefer, num_dos_compras_no_prefer, num_dos_compras_no_prefer_tarjeta,
               num_dos_compras_no_prefer_efectivo, num_dos_compras_no_prefer_mixto],
        color="violet"
    ))])

fig.update_layout(title_text="Flujo de clientes", font_size=10)
fig.show()
