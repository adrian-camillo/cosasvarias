## toda esta parte del codigo no va a poder continuarse porque dependo 100% de hacer de alguna forma, diferenciacion por genero.
## estoy intentando hacerlo con IA en base a los nombres de los clientes pero de momento no estaria funcionando


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

# calculate the age of each individual based on their birth date
today = pd.to_datetime("today").date()
df['age'] = (today - df['FECNAC'].dt.date) / pd.Timedelta(days=365.25)

# create age groups (e.g. 0-9, 10-19, 20-29, etc.)
df['age_group'] = (df['age'] // 10) * 10

# group the data by age group and gender
grouped = df.groupby(['age_group', 'gender']).size().reset_index(name='counts')

# plot the data for males and females
males = grouped[grouped['gender'] == 'Male']
females = grouped[grouped['gender'] == 'Female']

fig, ax = plt.subplots(nrows=2, figsize=(10, 10), gridspec_kw={'height_ratios': [5, 5]})

ax[0].barh(males['age_group'], males['counts'])
ax[0].set_title('Males')
ax[0].set_xlabel('Counts')
ax[0].set_ylabel('Age Group')

ax[1].barh(females['age_group'], females['counts'])
ax[1].set_title('Females')
ax[1].set_xlabel('Counts')
ax[1].set_ylabel('Age Group')

plt.tight_layout()
plt.savefig('population_pyramid.png')