import os
import pandas as pd

folder_path = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\Creditos_Marketing\archivos a csv'
output_folder = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\creditos\archivosprocesados'

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Obtener la lista de archivos CSV en la carpeta
file_list = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Recorrer cada archivo CSV y eliminar las columnas y definir tipos de datos
for file in file_list:
    file_path = os.path.join(folder_path, file)
    output_path = os.path.join(output_folder, file)
    df = pd.read_csv(file_path)  # Leer el archivo CSV en un DataFrame
    
    # Eliminar las columnas especificadas
    columns_to_drop = ['TELEFONO', 'TELEFONO1', 'TELEFONO2', 'MAIL', 'EDIRECC', 'EECALLE', 'ECODPOS', 'ELOCALI',
                       'EBARRIO', 'ETELEFO', 'ETELEFO1', 'CRECAN', 'CREACT', 'CREDITOS', 'SALDO', 'CAIDA', 'CAPITAL',
                       'INTERES', 'ENCAMARA', 'MAXATRASO', 'MAXATRACT', 'MORA', 'ULTPAGO', 'FECHATOPE', 'FECULTCRE',
                       'CMRMASCRE', 'CMRNOMBRE', 'CUPO', 'CUPOVENC', 'TIPO', 'NVOENPER', 'EMAIL', 'CANTREF', 'REFIACT',
                       'TARJETA', 'PARTIPO1', 'PARTELE1', 'PARNUME1', 'PARTITU1', 'PAROBSE1', 'PARTIPO2', 'PARTELE2',
                       'PARNUME2', 'PARTITU2', 'PAROBSE2', 'PARTIPO3', 'PARTELE3', 'PARNUME3', 'PARTITU3', 'PAROBSE3',
                       'LABTIPO1', 'LABTELE1', 'LABNUME1', 'LABTITU1', 'LABOBSE1', 'LABTIPO2', 'LABTELE2', 'LABNUME2',
                       'LABTITU2', 'LABOBSE2', 'MAIL_VALIDADO', 'mail_sugerido']
    df.drop(columns=columns_to_drop, inplace=True)  # Eliminar las columnas del DataFrame

    # Definir el tipo de datos de cada columna
    dtype_mapping = {
        'DNI': int,
        'NOMBRE': str,
        'FECNAC': 'datetime64[ns]',
        'DIRECCION': str,
        'ECALLES': str,
        'CODPOS': float,
        'LOCALIDAD': str,
        'BARRIO': str,
        'TELEFONO': str,
        'TELEFONO1': str,
        'TELEFONO2': str,
        'MAIL': str,
        'EMPRESA': str
    }
    df = df.astype(dtype_mapping)  # Aplicar el tipo de datos a cada columna

    df.to_csv(output_path, index=False)  # Guardar