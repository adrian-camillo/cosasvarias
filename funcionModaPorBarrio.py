import pandas as pd
import os

## all the hisotorical data segmented by 'provincia'
catamarcaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CATAM FEB23 (1).xlsx')
cbaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CBA FEB23 (1).xlsx')
laBandaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA LA BANDA FEB23 (1).xlsx')
mendozaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA MZA FEB23 (1).xlsx')
santiagoFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA STGO FEB23 (2).xlsx')
laRiojaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CATAM FEB23 (1).xlsx')

## Lists that will be use later
df_names = ["catamarcaFeb23Bruto", "cbaFeb23Bruto", "laBandaFeb23Bruto", 'mendozaFeb23Bruto', "santiagoFeb23Bruto",'laRiojaFeb23Bruto']
df_list = [catamarcaFeb23Bruto, cbaFeb23Bruto, laBandaFeb23Bruto, mendozaFeb23Bruto, santiagoFeb23Bruto, laRiojaFeb23Bruto]

## deberia de hacer un count con los 'barrio' de cada df en df_list y asignarle el valor a una variable scope global
#pero tambien deberia de guardarlo en excel con el nombre del barrio y el nombre de c/provincia a la que peretenece cada barrio, junto con el recuento de veces que aparece

# Combine dataframes
df = pd.concat(df_list, ignore_index=True)

# Unique localidades for validation
valid_localidades = ['cordoba','cba','arca' ,'catamarca','santiago','LA BANDA - SGO.DEL ESTERO','SGO', 'stgo', 'oza','mendoza', 'la banda', 'oja','rioja']

# Filter dataframe by valid localidades
df = df[df['LOCALIDAD'].str.lower().isin(valid_localidades)]

# Group by localidad and barrio and count occurrences
grouped_df = df.groupby(['LOCALIDAD', 'BARRIO']).size().reset_index(name='count')

# Export to excel files, one file for each localidad
for localidad in valid_localidades:
    localidad_df = grouped_df[grouped_df['LOCALIDAD'].str.lower() == localidad]
    if not localidad_df.empty:
        # Create folder if it doesn't exist
        folder_path = r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\output\{}'.format(localidad)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # Export to excel
        file_path = os.path.join(folder_path, '{}.xlsx'.format(localidad))
        localidad_df.to_excel(file_path, index=False)





#### Todavia no funciona, los resultados estan en la carpeta Output