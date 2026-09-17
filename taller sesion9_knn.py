"""
Taller Sesión 9: KNN (K-Nearest Neighbors)
Asignatura: Inteligencia Artificial II
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def ejecutar_laboratorio():
    # 1. Dataset ampliado: 10 clientes con 3 características [Edad, Salario, N° Hijos]
    X_entrenamiento = np.array([
        [20, 30, 0],  # Cliente 1
        [40, 50, 2],  # Cliente 2
        [35, 45, 1],  # Cliente 3
        [18, 25, 0],  # Cliente 4
        [50, 80, 3],  # Cliente 5
        [22, 32, 0],  # Cliente 6
        [45, 60, 2],  # Cliente 7
        [28, 40, 1],  # Cliente 8
        [60, 90, 4],  # Cliente 9
        [25, 28, 0]   # Cliente 10
    ])

    # 2. Etiquetas de clase: 0 = NO COMPRA, 1 = COMPRA
    Y_entrenamiento = np.array([0, 1, 1, 0, 1, 0, 1, 0, 1, 0])

    # 3. Nuevo cliente a evaluar: [Edad: 30, Salario: 40, Hijos: 1]
    nuevo_cliente = np.array([[30, 40, 1]])

    # 4. Evaluación con K = 1
    modelo_k1 = KNeighborsClassifier(n_neighbors=1)
    modelo_k1.fit(X_entrenamiento, Y_entrenamiento)
    pred_k1 = modelo_k1.predict(nuevo_cliente)

    # 5. Evaluación con K = 5
    modelo_k5 = KNeighborsClassifier(n_neighbors=5)
    modelo_k5.fit(X_entrenamiento, Y_entrenamiento)
    pred_k5 = modelo_k5.predict(nuevo_cliente)

    # Resultados
    clases = {0: "NO COMPRA", 1: "COMPRA"}
    print("=== RESULTADOS DEL MODELO KNN ===")
    print(f"Predicción para el nuevo cliente con K=1: {pred_k1[0]} ({clases[pred_k1[0]]})")
    print(f"Predicción para el nuevo cliente con K=5: {pred_k5[0]} ({clases[pred_k5[0]]})")

if __name__ == "__main__":
    ejecutar_laboratorio()
