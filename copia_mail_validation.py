import pandas as pd
import csv
import re
import os

# Carpeta de entrada y salida
carpeta_entrada = 'Creditos_Marketing/archivos a modificar/'
carpeta_salida = 'Creditos_Marketing/archivos a csv/'

# Lista de nombres de los archivos XLSX
archivos_xlsx = ['BASE CATAM JUNIO23.xlsx',
                 'BASE CBA JUNIO 2023.xlsx',
                 'BASE LA BANDA JUNIO23.xlsx',
                 'BASE LA RIOJA JUNIO23.xlsx',
                 'BASE SANTIAGO JUNIO23.xlsx',
                 'BASE MZA JUNIO23.xlsx']

def corregir_mail(mail):
    if isinstance(mail, str) and '@' in mail:
        # Detectar el dominio del correo electrónico
        usuario, dominio = mail.split('@', 1)

        # Verificar si el dominio es incorrecto
        if not dominio.endswith('.com') and not dominio.endswith('.com.ar'):
            if dominio.lower().startswith(('g','h','y')):
                if dominio.lower().startswith('g'):
                    dominio = 'gmail.com'
                elif dominio.lower().startswith('h'):
                    dominio = 'hotmail.com.ar'
                elif dominio.lower().startswith('y'):
                    dominio = 'yahoo.com'
        # Reconstruir el correo electrónico corregido
        mail_corregido = usuario + '@' + dominio
    else:
        mail_corregido = ''
    return mail_corregido

for archivo in archivos_xlsx:
    # Ruta completa del archivo de entrada
    ruta_entrada = os.path.join(carpeta_entrada, archivo)

    # Leer el archivo XLSX
    datos = pd.read_excel(ruta_entrada)

    # Renombrar la columna 'CLIENTE' a 'DNI'
    datos = datos.rename(columns={'CLIENTE': 'DNI'})

    # Eliminar el prefijo '1-' de los registros de la columna 'DNI'
    datos['DNI'] = datos['DNI'].str.replace('1-', '')
    
    # Corregir los correos y añadir columnas nuevas
    datos['MAIL'] = datos['MAIL'].apply(corregir_mail)
    datos['MAIL_VALIDADO'] = datos['MAIL'].apply(lambda x: True if re.match(r'^[a-zA-Z0-9_.]+[@]\w+[.]\w+$', x) else False)
    datos['mail_sugerido'] = datos.apply(lambda row: row['MAIL'] if row['MAIL_VALIDADO'] and "@" in row['MAIL'] else '', axis=1)
    
    # Generar el nombre del archivo CSV de salida
    nombre_csv = archivo.replace('.xlsx', '_corregido.csv')

    # Ruta completa del archivo de salida
    ruta_salida = os.path.join(carpeta_salida, nombre_csv)

    # Guardar los datos en formato CSV
    datos.to_csv(ruta_salida, index=False)

    print(f"Archivo {archivo} convertido, corregido y guardado en {ruta_salida} exitosamente.")

print("Corrección de mails completada.")