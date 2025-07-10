import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Create a dictionary with data
datos = {
   'Nombre': ['Ana', 'Luis', 'Carlos', 'Sofía', 'Pedro', 'María', 'Juan', 'Laura', 'Andrés', 'Camila'],
    'Puntaje': [88,    95,     79,      90,      85,      80,      92,     89,       76,      82],
    'Edad':    [25,    30,     22,      28,      26,      24,      29,     27,       21,      23],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla',
               'Bogotá', 'Cali', 'Medellín', 'Barranquilla',
               'Cali', 'Bogotá'],
    'Correo electrónico': [
        'ana@email.com', 'luis@email.com', 'carlos@email.com', 'sofia@email.com',
        'pedro@email.com', 'maria@email.com', 'juan@email.com', 'laura@email.com',
        'andres@email.com', 'camila@email.com'
    ]
}

# Create the Dataframe
df = pd.DataFrame(datos)


# Add columns of date Simulation
df['Fecha'] = pd.date_range(start='2024-01-01', periods=len(df), freq='M')

# Sort the objects by size
df = df.sort_values(by='Fecha')

# The line chart is sorted by age.
plt.figure(figsize=(6,4))
sns.lineplot(x='Fecha', y='Edad', data=df, marker='o')
plt.title("Tendencia de Edad a lo largo del tiempo")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""
# Scatter plot
plt.figure(figsize=(6,4))
sns.scatterplot(x='Edad', y='Puntaje', data=df)
plt.title("Relación entre Edad y Puntaje")
plt.xlabel("Edad")
plt.ylabel("Puntaje")
plt.tight_layout()
plt.show()


# bar chart
plt.figure(figsize=(6,4))
sns.countplot(x='Ciudad', data=df)
plt.title("Distribución por Ciudad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sort by column "Age"
#df_ordenado = df.sort_values(by='Edad')

# Show dataframe
#print(df)
#print(df_ordenado)


# Calculate the corelationship between Age and Score
correlacion = df['Edad'].corr(df['Puntaje'])

print("Correlación entre Edad y Puntaje:", correlacion)


# Group by city and calculate sum, mean, amount of people
resumen = df.groupby('Ciudad')['Edad'].agg([
    ('Suma de edades', 'sum'),
    ('Promedio de edad', 'mean'),
    ('Cantidad de personas', 'count')
])

#  Show the summary
print(resumen)


# Group by City and calculate statistics
estadisticas = df.groupby('Ciudad')['Edad'].agg(['mean', 'median', 'std']).rename(columns={
    'mean': 'Media',
    'median': 'Mediana',
    'std': 'Desviación estándar'
})

# Show statistics 
print(estadisticas)


# Count values NO null per column
conteo_columnas = df.count()

print(conteo_columnas) 

#  Use describe()
resumen = df.describe() #indica cuánto varían los datos con respecto a la media.

print(resumen)

datos = pd.Series([10, 20, 30, 40, 50])

# Quartiles
q1 = datos.quantile(0.25)
q2 = datos.quantile(0.5)   # Mediana
q3 = datos.quantile(0.75)

print("Q1 (25%):", q1)
print("Q2 (50% - mediana):", q2)
print("Q3 (75%):", q3)

import pandas as pd

# Replace with file path
df = pd.read_csv('username.csv')

# Show the firt rows
print(df.head())

#for Excel files
df = pd.read_excel('file_example_XLS_10.xls')
print(df)

#Count people by country
conteo = df['Country'].value_counts()

# Plot with Pandas
conteo.plot(kind='bar', figsize=(8, 5), color='lightgreen')
plt.title('Cantidad de personas por país')
plt.xlabel('País')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""