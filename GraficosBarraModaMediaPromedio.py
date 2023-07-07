import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import glob
from scipy import stats
import matplotlib.pyplot as plt
import os

def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

path = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\creditos\archivosprocesados\Archivos con edades'
graphs_path = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\creditos\Graficos'  # Asegúrate de que esta ruta exista
medians = []
means = []
modes = []

for file_name in glob.glob(path + "/*.csv"):
    df = pd.read_csv(file_name)
    df = df.loc[df['EDAD'] >= 18]
    base_name = os.path.basename(file_name) 
    base_name = os.path.splitext(base_name)[0] 
    base_name = base_name.replace('BASE', '').replace('JUNIO23_corregido', '') # Aquí está la corrección
    median_age = df['EDAD'].median()
    medians.append({'Archivo': base_name, 'Mediana de Edad': median_age})
    mean_age = df['EDAD'].mean()
    means.append({'Archivo': base_name, 'Promedio de Edad': mean_age}) 
    mode_age = df['EDAD'].mode().values[0]
    modes.append({'Archivo': base_name, 'Moda de Edad': mode_age})

df_medians = pd.DataFrame(medians)
df_means = pd.DataFrame(means)
df_modes = pd.DataFrame(modes)
data_files = {
    'Medianas': df_medians,
    'Promedios': df_means,
    'Modas': df_modes
}

for title, df in data_files.items():
    plt.figure(figsize=(10, 8))
    plt.bar(df['Archivo'], df[df.columns[1]], color='skyblue')
    plt.xlabel('Region')
    plt.ylabel(df.columns[1])
    plt.title(f'{df.columns[1]} por region')
    plt.xticks(rotation=90)
    plt.savefig(graphs_path + f'/{title}.png', bbox_inches='tight')
    plt.show()