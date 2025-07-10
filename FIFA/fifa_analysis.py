import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('male_players.csv')

# Filter Messi and Cristiano Ronaldo
jugador_1 = df[df['long_name'] == 'Lionel Andrés Messi Cuccittini']
jugador_2 = df[df['long_name'] == 'Cristiano Ronaldo dos Santos Aveiro']

# Show labels (columns)
print(df.columns) 

# Verify that the column exists
print("Columnas disponibles:", df.columns.tolist())

# Calculate averages
messi_passing = jugador_1['passing'].astype(float).mean()
ronaldo_passing = jugador_2['passing'].astype(float).mean()

# Create comparative DataFrame
df_passing = pd.DataFrame({
    'Jugador': ['Messi', 'Cristiano Ronaldo'],
    'Passing': [messi_passing, ronaldo_passing]
})

# Graph
#canvas size
plt.figure(figsize=(6, 5))
sns.barplot(data=df_passing, x='Jugador', y='Passing', palette='Blues')

plt.title('Comparación de Passing: Messi vs Cristiano Ronaldo')
plt.ylabel('Valor de Passing')
plt.ylim(0, 100)
plt.tight_layout()
plt.show()



