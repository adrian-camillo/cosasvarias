import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

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

# convert the date column to a datetime format
df['FECNAC'] = pd.to_datetime(df['FECNAC'], format='%d/%m/%Y')

# keep only the rows with date values between 01/01/1900 and 01/01/2024
df = df.loc[(df['FECNAC'] >= pd.to_datetime("01/01/1900", format='%d/%m/%Y')) &
            (df['FECNAC'] <= pd.to_datetime("01/01/2024", format='%d/%m/%Y'))]

# extract the year from the datetime column
df['year'] = df['FECNAC'].dt.year

# group the data by ranges of 10 years
df['decade'] = (df['year'] // 10) * 10

# count the number of observations in each decade range
decade_counts = df.groupby('decade').size().reset_index(name='counts')

print(decade_counts)

# plot the data using bar chart
plt.bar(decade_counts['decade'], decade_counts['counts'])
plt.xlabel('Decade')
plt.ylabel('Counts')
plt.savefig('plot.png')

