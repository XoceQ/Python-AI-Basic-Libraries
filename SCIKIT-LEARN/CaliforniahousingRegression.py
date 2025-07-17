from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# 1. Cargar el dataset
california = fetch_california_housing()
X = california.data  # Características
y = california.target  # Variable objetivo (precio mediano de vivienda en cientos de miles de dólares)

# 2. Dividir en train/test (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Crear y entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Evaluar el modelo
y_pred = model.predict(X_test)

print("Métricas de evaluación:")
print(f"- Error Cuadrático Medio (MSE): {mean_squared_error(y_test, y_pred):.2f}")
print(f"- Coeficiente de Determinación (R²): {r2_score(y_test, y_pred):.2f}")

# 5. Mostrar coeficientes del modelo
feature_names = california.feature_names
coef_df = pd.DataFrame({
    'Característica': feature_names,
    'Coeficiente': model.coef_
}).sort_values('Coeficiente', ascending=False)

print("\nCoeficientes del modelo:")
print(coef_df)
print(f"\nTérmino independiente (intercept): {model.intercept_:.2f}")