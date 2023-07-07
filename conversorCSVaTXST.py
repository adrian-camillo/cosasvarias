import pandas as pd

# cargar archivo CSV en un DataFrame
dataframe = pd.read_csv('C:\Users\adrian\Desktop\base de datos Nico-Calzados\CalculadorGanancias\publicaciones.csv')

dataframe2 = pd.read_csv('C:\Users\adrian\Desktop\base de datos Nico-Calzados\CalculadorGanancias\stock.csv')

# guardar DataFrame en formato Excel
dataframe.to_excel('datos.xlsx', index=False)
dataframe2.to_excel('datos.xlsx', index=False)
