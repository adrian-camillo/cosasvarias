import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
ruta_archivo = r'Analisis_HotSale\analisis hotsale 20203 - reporte_de_ventas (9).csv.csv'
df = pd.read_csv(ruta_archivo, sep=',')

# Convertir la columna 'Fecha' a formato datetime y crear una columna con la fecha en formato "día/mes"
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
df['Fecha_dia_mes'] = df['Fecha'].dt.strftime('%d/%m')

# Agrupar los datos por fecha y sumar los valores de 'Imp. Total' y 'Imp. Total Acumulado'
df_grouped = df.groupby('Fecha_dia_mes')['Imp. Total'].sum().reset_index()
df_grouped['Imp. Total Acumulado'] = df_grouped['Imp. Total'].cumsum()

# Crear el gráfico de barras
sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize=(12, 6))

# Obtener los datos para las barras
fechas = df_grouped['Fecha_dia_mes']
montos_acumulados = df_grouped['Imp. Total Acumulado']
montos_diarios = df_grouped['Imp. Total']

# Crear la barra de montos diarios
ax.bar(fechas, montos_diarios, color='blue', alpha=0.8, label='Monto diario')

# Crear la barra de montos acumulados
ax.bar(fechas, montos_acumulados, color='grey', alpha=0.5, label='Monto acumulado')

# Configurar el gráfico
ax.set_xlabel('Fecha')
ax.set_ylabel('Monto')
ax.set_title('Distribución del importe total acumulado y diario')
ax.legend(loc='upper left')

# Ajustar los límites del eje y
ax.set_ylim([0, df_grouped['Imp. Total Acumulado'].max() * 1.1])

# Rotar las etiquetas del eje x
plt.xticks(rotation=45)

plt.show()







#testing
print(df['Imp. Total'].unique())


# Convertir la columna 'Imp. Total' a un tipo numérico
df['Imp. Total'] = pd.to_numeric(df['Imp. Total'], errors='coerce')

# Filtrar los valores negativos de la columna 'Imp. Total'
imp_total_negativos = df[df['Imp. Total'] < 0]['Imp. Total']

# Contar la cantidad de valores negativos
cant_negativos = len(imp_total_negativos)

# Imprimir el resultado
print('La cantidad de valores negativos en la columna "Imp. Total" es:', cant_negativos)

