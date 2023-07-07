import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

catamarcaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CATAM FEB23 (1).xlsx')
cbaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CBA FEB23 (1).xlsx')
laBandaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA LA BANDA FEB23 (1).xlsx')
mendozaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA MZA FEB23 (1).xlsx')
santiagoFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA STGO FEB23 (2).xlsx')
laRiojaFeb23Bruto = pd.read_excel(r'C:\Users\adrian\Desktop\base de datos Nico-Calzados\SEGMENTA CATAM FEB23 (1).xlsx')

## lista de tablas
df_list = [catamarcaFeb23Bruto, cbaFeb23Bruto, laBandaFeb23Bruto, mendozaFeb23Bruto, santiagoFeb23Bruto, laRiojaFeb23Bruto]
df_names = ["catamarcaFeb23Bruto", "cbaFeb23Bruto", "laBandaFeb23Bruto", 'mendozaFeb23Bruto', "santiagoFeb23Bruto",'laRiojaFeb23Bruto']

# combine all dataframes into a single dataframe
df = pd.concat(df_list)

##trying to show a hist of 'SALDO' column
df['SALDO'].plot.bar(x='SALDO', rot=0)
plt.show()
plt.savefig("histOfSaldoss.png")