from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.interpolate import interp1d
import seaborn as sns

""" # We define the objective function
def f(x):
    return (x[0] - 3)**2 + 2

# Initial value (starting point)
x0 = [0]

# We call minimize()
# Gradient-based optimization algorithm
result = minimize(f, x0, method='BFGS')

# We display the result
print("Result:", result)
print("Minimum value of x:", result.x)
print("Minimum value of the function:", result.fun) 

# Data
x = np.array([0, 1, 2, 3])
y = np.array([0, 2, 4, 6])

# Creamos la función de interpolación lineal
f_interp = interp1d(x, y, kind='linear')

# Usamos la función para interpolar en x = 1.5
x_interp = 1.5
y_interp = f_interp(x_interp)

# Graphic
plt.plot(x, y, 'o-', label='Datos originales')
plt.plot(x_interp, y_interp, 'ro', label=f'Interpolado (x={x_interp}, y={y_interp:.1f})')
plt.axvline(x_interp, color='gray', linestyle='--', linewidth=0.8)
plt.axhline(y_interp, color='gray', linestyle='--', linewidth=0.8)
plt.title('Interpolación lineal en x = 1.5')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
"""

# Read the CSV file (adjust the name or path if needed)
df = pd.read_csv("Salary_Data.csv")

# Select only numeric columns
df_numericas = df.select_dtypes(include='number')

# Calculate Pearson correlation
correlacion = df_numericas.corr(method='pearson')
print(correlacion)

# Plot heatmap
plt.figure(figsize=(10, 8))  # Figure size
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Pearson Correlation Matrix')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
