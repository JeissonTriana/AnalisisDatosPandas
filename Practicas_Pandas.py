import pandas as pd

#series de pandas
numeros = [3, 4, 5, 7, 8]
print(numeros)

serie = pd.Series(numeros)
print(serie, type(serie))

#Dataframe
data = {
    "Nombre":["Jeisson", "Camilo", "Diego", "Miguel"],
    "Edad": [22, 25, 28, 23],
    "Ciudad": ["Medellin","Pereira","Bogota","Cali"]
}

#Generar un DataFrame a partir de un diccionario 

df = pd.DataFrame(data=data)
print(df)

#Exportar un DataFrame 
df.to_csv("DataTest.csv")

#importar un DataFrame
import_df = pd.read_csv("DataTest.csv",index_col=0)

#Seleccionar una columna
nombres = df["Nombre"]
print("\n")
print(nombres , type(nombres))

#Seleccionar una o mas columnas
print("\n")
datos = df[["Nombre","Ciudad"]]
print(datos)

#Filtrar por indice 
fila = df.loc[0]
print(fila)

#Filtrar por condicion 
print("\n")
edad = df[df["Edad"]>=25]
print(edad)

#Filtro compuesto
print("\n")
filtro = (df["Edad"]<=25) & (df["Nombre"].str.startswith("J"))
df[filtro]
print(df)