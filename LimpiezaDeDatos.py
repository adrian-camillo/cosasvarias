#cambio de xlsx a csv
import pandas as pd

# import pandas as pd

ruta_csv = "analisis retail\Trabajables\marketing\BASE CBA JUNIO 2023.csv"
df = pd.read_csv(ruta_csv)

# Rellenar valores faltantes en columnas numéricas con el promedio
df.fillna(df.mean(), inplace=True)

# Rellenar valores faltantes en columnas categóricas con el valor "Desconocido"
df.fillna("Desconocido", inplace=True)
df = df.fillna("Desconocido")

# Ver las primeras filas del DataFrame
df.head()

# Obtener información sobre las columnas y los tipos de datos
df.info()

# Obtener estadísticas descriptivas
df.describe()

# Manejo de valores faltantes
df.fillna('FALTANTE')  # Rellenar valores faltantes con un valor específico

# Eliminación de columnas no relevantes
#df.drop(["columna1", "columna2"], axis=1, inplace=True)  # Eliminar columnas específicas

# Transformación de tipos de datos
print(df)
df["CODPOS"] = pd.to_numeric(df["CODPOS"], errors="coerce")
df["CRECAN"] = pd.to_numeric(df["CRECAN"], errors="coerce")
df["CREACT"] = pd.to_numeric(df["CREACT"], errors="coerce")
df["CREDITOS"] = pd.to_numeric(df["CREDITOS"], errors="coerce")
df["SALDO"] = pd.to_numeric(df["SALDO"], errors="coerce")
print(df)
# Continuamos con las demas columnas
df.rename(columns={"CLIENTE": "DNI"}, inplace=True)
#modificando el formato de el dni 
df["DNI"] = df["DNI"].str.replace(r"^1-", "")


# Manejo de valores atípicos
#df = df[df["columna"] < valor_limite]  # Filtrar filas basado en un valor límite

# Cálculo de estadísticas adicionales
df["columna"].mean()  # Calcular el promedio de una columna
df["LOCALIDAD"].value_counts()  # Contar los valores únicos en una columna

# Agrupación de datos
df.groupby("columna").sum()  # Agrupar por una columna y sumar los valores

# Aplicación de funciones a columnas
#df["nueva_columna"] = df["columna"].apply(funcion)  # Aplicar una función a una columna y guardar el resultado en una nueva columna

# Visualización de resultados
import matplotlib.pyplot as plt
df["columna"].plot.hist()  # Crear un histograma de una columna
plt.show()


# DF codigos postales
codpos_counts_df = df['CODPOS'].value_counts().reset_index()
codpos_counts_df.columns = ['CODPOS', 'Count']
print(codpos_counts_df)
#codpos_counts_df.to_csv('codpos_counts.csv', index=False)


# DF localidades 
df["LOCALIDAD"].value_counts()  # Contar los valores únicos en una columna
Localidades_df = df["LOCALIDAD"].value_counts() .reset_index()
Localidades_df.columns = ['LOCALIDAD', 'Count']
print(Localidades_df)
#Localidades_df.to_csv('Localidades_df.csv', index=False)


df["CMRNOMBRE"].value_counts()  # Contar los valores únicos en una columna
CMRNOMBRE = df["CMRNOMBRE"].value_counts() .reset_index()
CMRNOMBRE.columns = ['CMRNOMBRE', 'Count']
print(CMRNOMBRE)
#CMRNOMBRE.to_csv('CMRNOMBRE.csv', index=False)


import pandas as pd
import matplotlib.pyplot as plt

ruta_csv = "analisis retail\Trabajables\marketing\BASE CBA JUNIO 2023.csv"
df = pd.read_csv(ruta_csv)

# Rellenar valores faltantes
df.fillna(df.mean(), inplace=True)  # Numerical columns
df.fillna("Desconocido", inplace=True)  # Categorical columns

# Transformación de tipos de datos
for col in ["CODPOS", "CRECAN", "CREACT", "CREDITOS", "SALDO"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Renombrando y formateando la columna
df.rename(columns={"CLIENTE": "DNI"}, inplace=True)
df["DNI"] = df["DNI"].str.replace(r"^1-", "")

# Creando gráficos para cada columna y guardando conteos en archivos csv
for column in ["CODPOS", "LOCALIDAD", "CMRNOMBRE"]:
    # Creando DataFrame de conteos
    counts_df = df[column].value_counts().reset_index()
    counts_df.columns = [column, 'Count']
    print(counts_df)
    
    # Guardando los conteos en un csv
    counts_df.to_csv(f'{column}_counts.csv', index=False)
    
    # Creando y mostrando histograma
    plt.hist(df[column].dropna(), bins=20, alpha=0.5)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()