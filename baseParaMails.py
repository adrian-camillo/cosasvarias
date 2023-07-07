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

## filter function to separate the values that meet the condition 
def filter_dataframe(df, df_names, crecan_condition, creact_condition,cupo):
    try:
        filtered_df = df.query(f"CRECAN >= {crecan_condition} and CREACT >= {creact_condition} and CUPOVENC >= {cupo}  ")
        ## save files, but it gives error.!!!!!!!!!!!!!!!!!!!!
        filtered_df.to_excel(f"C:\\Users\\adrian\\Desktop\\base de datos Nico-Calzados\\liquidacion\\{df_names}.xlsx", sheet_name='Sheet1', engine='openpyxl')
        return filtered_df
    except Exception as e:
        print("Error:", e)


## loop through the list of dataframes and apply the filter_dataframe function to each of them
for i, df in enumerate(df_list):
    filter_dataframe(df, df_names[i], 1,1, 15000)


## ´Para saber cuantos mail se van a mandar 
# Defino variable de almacenamiento 
CantidadTotalDeMails=()
# un buclecito que me recorre la lista 
for i in df_list:
    print(i.shape)
    CantidadTotalDeMails = CantidadTotalDeMails + i.shape[0]
# CantidadTotalDeMails print concatenated with an ilustrative text
print('la cantidad total de mails a mandar es: ' + str(CantidadTotalDeMails))