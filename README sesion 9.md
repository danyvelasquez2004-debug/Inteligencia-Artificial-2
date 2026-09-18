# Taller Práctico: Algoritmo KNN (K-Nearest Neighbors)

**Asignatura:** Inteligencia Artificial II  
**Tema:** Clasificación mediante el Algoritmo de K-Vecinos Más Cercanos  

---

## 1. Taller Analítico: La Votación Espacial

### Datos Iniciales
* **Cliente 1 (A):** $(20, 30) \rightarrow$ **NO COMPRA** (Clase 0)
* **Cliente 2 (B):** $(40, 50) \rightarrow$ **COMPRA** (Clase 1)
* **Cliente 3 (C):** $(35, 45) \rightarrow$ **COMPRA** (Clase 1)
* **Punto Nuevo (P):** $(30, 40)$

---

### Cálculos Matemáticos (Distancia Euclidiana)

Fórmula general:
$$d(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

1. **Distancia a Cliente A:**
   $$d(P, A) = \sqrt{(30-20)^2 + (40-30)^2} = \sqrt{100 + 100} = \sqrt{200} \approx 14.14$$

2. **Distancia a Cliente B:**
   $$d(P, B) = \sqrt{(30-40)^2 + (40-50)^2} = \sqrt{100 + 100} = \sqrt{200} \approx 14.14$$

3. **Distancia a Cliente C:**
   $$d(P, C) = \sqrt{(30-35)^2 + (40-45)^2} = \sqrt{25 + 25} = \sqrt{50} \approx 7.07$$

---

### Resultados de Clasificación

* **Caso $K = 1$:**  
  El vecino más cercano es **C** ($d = 7.07$).  
  **Clasificación final:** **COMPRA**

* **Caso $K = 3$:**  
  Los 3 vecinos más cercanos son **C** (COMPRA), **A** (NO COMPRA) y **B** (COMPRA).  
  Votación: 2 Votos COMPRA vs. 1 Voto NO COMPRA.  
  **Clasificación final:** **COMPRA**

* **Conclusión:** No hubo cambio en la decisión al variar $K$ entre 1 y 3.

---

## 2. Taller de Laboratorio

### La Maldición de la Dimensionalidad

**¿Qué ocurre con la Distancia Euclidiana si pasamos de 3 dimensiones a 1,000 dimensiones?**

1. **Concentración de Distancias:** En espacios de alta dimensionalidad, el volumen crece exponencialmente, provocando que los datos se vuelvan extremadamente dispersos. Matemáticamente, la distancia entre un punto y su vecino más cercano empieza a converger con la distancia hacia el punto más lejano.
2. **Pérdida de Efectividad:** Dado que la diferencia entre distancias se vuelve insignificante, el concepto de "proximidad" o "vecindad" pierde sentido, reduciendo la precisión de clasificadores basados en distancia como KNN.
3. **Costo Computacional:** El cómputo de distancias a través de miles de dimensiones para cada predicción degrada significativamente el rendimiento del sistema.
