import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import glob

# Función para calcular la edad
def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# Ubicación de tus archivos
path = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\creditos\archivosprocesados'

# DataFrame para almacenar las filas con fechas fuera de rango
df_out_of_range = pd.DataFrame()

# Recorre cada archivo CSV en la carpeta
for file_name in glob.glob(path + "/*.csv"):
    # Lee el archivo CSV
    df = pd.read_csv(file_name)

    # Intenta convertir la columna de fecha de nacimiento a un formato de fecha
    df['FECNAC'] = pd.to_datetime(df['FECNAC'], format='%Y/%m/%d', errors='coerce')

    # Almacena las filas con fechas fuera de rango en df_out_of_range
    df_out_of_range = df_out_of_range.append(df[df['FECNAC'].isna()])

    # Elimina las filas con fechas fuera de rango del DataFrame original
    df = df.dropna(subset=['FECNAC'])

    # Aplica la función para calcular la edad
    df['EDAD'] = df['FECNAC'].apply(calculate_age)

    # Guarda el dataframe modificado al mismo archivo CSV
    df.to_csv(file_name, index=False)

# Guarda las filas con fechas fuera de rango en un archivo CSV
df_out_of_range.to_csv(path + "/fechas_fuera_de_rango.csv", index=False)





## GRAFICOS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# Función para calcular el rango de edad
def calculate_age_range(age):
    try:
        return f'{age//2*2}-{age//2*2+1}'
    except:
        return 'Desconocido'

def convert_to_int(s):
    try:
        return int(s)
    except ValueError:
        return np.nan

path = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\creditos\archivosprocesados'
medians = []
graphs_path = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\creditos\Graficos'

# Recorre cada archivo CSV en la carpeta
for file_name in glob.glob(path + "/*.csv"):
    df = pd.read_csv(file_name)
    
    # Elimina las filas con edades menores a 18
    df = df.loc[df['EDAD'] >= 18]
    
    # Calcula la edad media y la agrega a la lista de medianas
    median_age = df['EDAD'].median()
    medians.append({'Archivo': os.path.basename(file_name), 'Mediana de Edad': median_age})
    
    # Calcula el rango de edad y cuenta el número de personas en cada rango
    df['Rango de Edad'] = df['EDAD'].apply(calculate_age_range)
    age_counts = df['Rango de Edad'].value_counts()

    # Ordena los rangos de edades como números en lugar de cadenas de texto
    age_counts = age_counts.reset_index().rename(columns={'index': 'Rango de Edad', 'Rango de Edad': 'Número de personas'})
    age_counts['Edad mínima'] = age_counts['Rango de Edad'].str.split('-').str[0].apply(convert_to_int)
    age_counts = age_counts.sort_values('Edad mínima')
    
    # Obtiene el título del gráfico a partir del nombre del archivo
    title = os.path.basename(file_name).replace('BASE', '').replace('JUNIO23_corregido.csv', '')
    
    # Genera la pirámide poblacional
    plt.figure(figsize=(10, 8))
    plt.barh(age_counts['Rango de Edad'], age_counts['Número de personas'], color='skyblue')
    plt.xlabel('Número de personas')
    plt.ylabel('Rango de Edad')
    plt.title(f'Pirámide poblacional del archivo {title}')
    
    # Guarda el gráfico en un archivo .png
    plt.savefig(graphs_path + f'/{title}.png')
    plt.show()

# Guarda las medianas en un nuevo archivo CSV
df_medians = pd.DataFrame(medians)
df_medians.to_csv(path + "/medianas.csv", index=False)










