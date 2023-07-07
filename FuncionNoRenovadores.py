import pandas as pd
from collections import Counter

catamarcaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CATAM FEB23 (1).xlsx')
cbaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CBA FEB23 (1).xlsx')
laBandaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA LA BANDA FEB23 (1).xlsx')
mendozaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA MZA FEB23 (1).xlsx')
santiagoFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA STGO FEB23 (2).xlsx')
laRiojaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CATAM FEB23 (1).xlsx')

## lista de tablas
df_list = [catamarcaFeb23Bruto, cbaFeb23Bruto, laBandaFeb23Bruto, mendozaFeb23Bruto, santiagoFeb23Bruto, laRiojaFeb23Bruto]
df_names = ["catamarcaFeb23Bruto", "cbaFeb23Bruto", "laBandaFeb23Bruto", 'mendozaFeb23Bruto', "santiagoFeb23Bruto",'laRiojaFeb23Bruto']

## funcion que retorna valores de una tabla ordenados por la ' moda ' o por el recuento de veces que aparece

def mode_of_barrios_in_tables(tables):
    mode_of_barrios = []
    for table in tables:
        barrios = table['BARRIO'].value_counts()
        mode_of_barrios.append(barrios)
    return mode_of_barrios

tables = df_list # Replace with other list of tables if you want  
result = mode_of_barrios_in_tables(tables)

##call a la funcion de arriba
barrios_mode = mode_of_barrios_in_tables(df_list)
print('La lista de barrios que mas saca credito son:', barrios_mode)

# Save the result to an Excel file
output_writer = pd.ExcelWriter("barrios_mode.xlsx", engine='openpyxl')
for i, barrios_mode in enumerate(result):
    barrios_mode.to_excel(output_writer, sheet_name=f"Sheet{i+1}")
output_writer.save()
