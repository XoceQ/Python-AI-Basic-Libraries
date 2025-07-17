from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Cargar y dividir los datos
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Crear y entrenar el modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)  # Usando 3 vecinos
knn.fit(X_train, y_train)

# 3. Realizar predicciones
y_pred = knn.predict(X_test)

# 4. Evaluar el modelo
print("Exactitud (Accuracy):", accuracy_score(y_test, y_pred))
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))