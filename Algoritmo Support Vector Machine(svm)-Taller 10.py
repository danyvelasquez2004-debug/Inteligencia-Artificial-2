Taller: Algoritmo Support Vector Machine (SVM) - SESIÓN 10
Estudiante: Daniel Fernando Velasquez Moreno
Fecha: 21 sept 2026
Asignatura: Inteligencia Artificial II
Institución: Institución Universitaria de Colombia
Parte 1: Taller Analítico - Puntos del Conjunto de Datos
Clase
Etiqueta
Coordenadas
Clase A (Círculos)
0
(2,2), (3,3), (4,2)
Clase B (Equis)
1
(6,6), (7,8), (8,7)

1. Línea Recta Óptima (Hiperplano de Separación)
Para determinar el hiperplano óptimo, identificamos los puntos más cercanos entre ambas clases. Estos puntos son (3,3) de la Clase A y (6,6) de la Clase B.

La línea que maximiza el margen se sitúa exactamente en el punto medio de la distancia entre estos vectores. La ecuación resultante es:

y = -x + 9 o, en su forma general, x + y - 9 = 0

Esta recta separa perfectamente ambos grupos, estableciendo un margen de separación ("calle") equidistante de los vectores de soporte.
2. Vectores de Soporte
Los Vectores de Soporte son los puntos críticos que definen la geometría del margen. Si estos puntos se eliminaran, la posición del hiperplano cambiaría. En este conjunto de datos, los vectores son:

Clase A: (3,3)
Clase B: (6,6)

Nota: En una representación gráfica, estos son los únicos puntos que deben marcarse con un círculo de énfasis (ej. rojo) para indicar su función como limitadores del margen.
3. Análisis de Sensibilidad: Punto (1,1)
Pregunta: ¿Cambiaría la posición de la línea si añadimos el punto (1,1) a la Clase A?

Respuesta: No, la posición de la línea no cambiaría.

Justificación Teórica: El algoritmo SVM se fundamenta en la maximización del margen a través de los Vectores de Soporte. Cualquier punto que se encuentre fuera de las líneas de frontera del margen (hacia el interior de su propia clase) es irrelevante para la definición del hiperplano. Como el punto (1,1) es más lejano a la frontera que el punto (3,3), no ejerce presión sobre el margen y, por lo tanto, no altera el modelo.
Parte 2: Taller de Laboratorio - Fronteras No Lineales
1. Verificación de Vectores de Soporte con Python
Al implementar el modelo en Scikit-Learn utilizando un kernel lineal, el sistema identifica automáticamente los puntos de control.import numpy as np

from sklearn.svm import SVC

X = np.array([[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7]])

Y = np.array([0, 0, 0, 1, 1, 1])

modelo_svm = SVC(kernel="linear")

modelo_svm.fit(X, Y)

vectores = modelo_svm.support_vectors_

print("Los Vectores de Soporte son:\n", vectores)

Resultado obtenido:Los Vectores de Soporte son:

 [[3. 3.]

  [6. 6.]]

Este resultado valida matemáticamente el análisis realizado en la Parte 1.
2. Modificación del Dataset y Comparación de Kernels
Se introduce una perturbación en los datos: un punto de la Clase A ubicado en (5,5), el cual se encuentra geográficamente más cerca de la Clase B, rompiendo la separabilidad lineal.import numpy as np

from sklearn.svm import SVC

# Agregar el punto [5,5] con etiqueta 0 (Clase A)

X = np.array([[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7], [5, 5]])

Y = np.array([0, 0, 0, 1, 1, 1, 0])

# Entrenamiento con Kernel Lineal

modelo_lineal = SVC(kernel="linear")

modelo_lineal.fit(X, Y)

# Entrenamiento con Kernel RBF (Función de Base Radial)

modelo_rbf = SVC(kernel="rbf")

modelo_rbf.fit(X, Y)

print("--- RESULTADOS DE PREDICCIÓN PARA [5,4] ---")

print("Predicción Kernel Lineal:", modelo_lineal.predict(np.array([[5, 4]]))[0])

print("Predicción Kernel RBF:   ", modelo_rbf.predict(np.array([[5, 4]]))[0])
Observaciones de Comportamiento
Kernel Lineal: Al intentar trazar una línea recta en un conjunto que ya no es linealmente separable, el modelo se ve forzado a aceptar errores de clasificación o a desplazar drásticamente su frontera, perdiendo precisión.
Kernel RBF: Mediante el Kernel Trick, el algoritmo proyecta los datos a un espacio de mayor dimensión donde es posible encerrar o aislar el punto (5,5). Esto genera una frontera curva que se adapta a la distribución real de los datos.
Parte 3: Reflexión y Escenarios del Mundo Real
1. Diagnóstico Médico (Detección de Tumores)
En la práctica clínica, los valores metabólicos considerados "normales" suelen estar concentrados en rangos específicos. Las patologías pueden manifestarse tanto por exceso como por defecto de ciertos indicadores, rodeando la "zona saludable" en un espacio multidimensional. Un Kernel RBF es indispensable aquí para crear fronteras de decisión cerradas o elípticas que separen lo sano de lo patológico.
2. Reconocimiento Facial y Biometría
Las características faciales no varían de forma lineal; factores como la iluminación, el ángulo y la oclusión generan nubes de datos complejas y entrelazadas. Para diferenciar un rostro específico entre miles, se requieren fronteras altamente complejas y no lineales que solo kernels como el RBF o el polinómico pueden proporcionar de manera efectiva.
