import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as seabornInstance 

df = pd.read_csv('analisis retail\ReporteDeVentasDiciembre2022Hasta15Mayo2023.csv')

# Clean the data
df['Imp. Total'] = df['Imp. Total'].str.replace('"', '').str.replace('.', '').str.replace(',', '.').str.replace('$', '').astype(float)

df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Fecha'] = (df['Fecha'] - df['Fecha'].min())  / np.timedelta64(1,'D')

# Define feature matrix and target vector
X = df['Fecha'].values.reshape(-1,1)
y = df['Imp. Total'].values.reshape(-1,1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and fit the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regressor.predict(X_test)

# Plot the results
plt.scatter(X_test, y_test,  color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('Dias')
plt.ylabel('Montos')
plt.title('Progresion Lineal')
plt.savefig('grafico12.png')
plt.close()


import pandas as pd
import numpy as np
# Clean the data
df['Imp. Total'] = df['Imp. Total'].replace('[\$,\""]', '', regex=True).replace(',', '.', regex=True).astype(float)
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Define cohorts
df.set_index('DNI / CUIT', inplace=True)
df['Cohorte'] = df.groupby(level=0)['Fecha'].min().apply(lambda x: x.strftime('%Y-%m'))
df.reset_index(inplace=True)

# Store analysis
store_analysis = df.groupby('Nro Suc').agg({'Imp. Total':'sum'}).sort_values('Imp. Total', ascending=False)

# CLV analysis
clv_analysis = df.groupby('DNI / CUIT').agg({'Imp. Total':'sum'}).sort_values('Imp. Total', ascending=False)
# Plot the CLV analysis
plt.figure(figsize=(10, 6))  # Set the figure size

# Create the bar plot
clv_analysis.plot(kind='barh', legend=False)
plt.xlabel('Imp. Total')  # X-axis label
plt.ylabel('DNI / CUIT')  # Y-axis label
plt.title('Customer Lifetime Value Analysis')  # Plot title

plt.savefig('grafico11.png')
plt.close()
# Retention analysis
retention_analysis = df.groupby(['Cohorte', 'Fecha']).agg({'DNI / CUIT':'nunique'}).reset_index()
retention_analysis['Period'] = (retention_analysis['Fecha'].dt.year - pd.to_datetime(retention_analysis['Cohorte']).dt.year)*12 + (retention_analysis['Fecha'].dt.month - pd.to_datetime(retention_analysis['Cohorte']).dt.month)
retention_pivot = retention_analysis.pivot_table(index='Cohorte', columns='Period', values='DNI / CUIT')

# Correlation analysis
correlation_analysis = df.corr()

# Print the analysis
print("Store Analysis:\n", store_analysis)
print("\nCustomer Lifetime Value Analysis:\n", clv_analysis)
print("\nRetention Analysis:\n", retention_pivot)
print("\nCorrelation Analysis:\n", correlation_analysis)

import matplotlib.pyplot as plt


# Count the frequency of each card type
# Filter out '-' and '---' registers
filtered_df = df[df['Tarjeta tipo'].isin(['"-"', '"---"']) == False]

# Count the frequency of each card type
card_counts = filtered_df['Tarjeta tipo'].value_counts()

# Create the pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(card_counts, labels=card_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Card Types (Excluding "-" and "---")')

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.savefig('grafico10.png')
plt.close()



