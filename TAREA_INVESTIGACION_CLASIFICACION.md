# Tarea: Investigación y Desarrollo de Algoritmos de Clasificación en Machine Learning Supervisado

**Autor:** Paloma Gómez Salazar  
**Fecha:** 25 de Febrero de 2026

---

## Parte 1: Algoritmos de Clasificación en ML Supervisado

### 1. ¿Qué es la clasificación en Machine Learning y cuál es su propósito?

#### Definición
La **clasificación** en Machine Learning es una técnica de aprendizaje supervisado que consiste en predecir la categoría o clase a la que pertenece una observación basándose en sus características. El algoritmo aprende patrones de un conjunto de datos etiquetados (datos de entrenamiento) para luego poder asignar etiquetas a nuevos datos no vistos.

#### Propósito
El propósito principal de la clasificación es:
- **Automatizar la toma de decisiones** basándose en patrones aprendidos
- **Categorizar datos** de manera eficiente y precisa
- **Predecir resultados discretos** (clases o categorías)
- **Identificar patrones complejos** que serían difíciles de detectar manualmente

#### Ejemplo Práctico del Mundo Real

**Problema:** Detección de Fraude en Transacciones Bancarias

**Contexto:**  
Los bancos procesan millones de transacciones diarias y necesitan identificar automáticamente cuáles son fraudulentas para proteger a sus clientes.

**Aplicación:**
- **Datos de entrada:** Monto de la transacción, ubicación, hora, tipo de comercio, historial del cliente, etc.
- **Clases:** "Transacción Legítima" vs "Transacción Fraudulenta"
- **Objetivo:** Clasificar cada transacción en tiempo real para bloquear operaciones sospechosas

**Beneficios:**
- Reducción de pérdidas económicas por fraude
- Protección inmediata de los clientes
- Análisis de millones de transacciones en segundos
- Mejora continua del modelo con nuevos datos

---

### 2. ¿Cuál es la diferencia entre clasificación binaria y multiclase?

#### Clasificación Binaria

**Definición:**  
La clasificación binaria es cuando el modelo predice entre **dos clases posibles** (generalmente representadas como 0 y 1, o positivo y negativo).

**Características:**
- Solo hay dos categorías mutuamente excluyentes
- El resultado es binario: Sí/No, Verdadero/Falso, Clase A/Clase B
- Más simple de implementar y evaluar

**Ejemplos:**

1. **Diagnóstico Médico**
   - Clases: "Enfermo" vs "Sano"
   - Aplicación: Detectar si un paciente tiene una enfermedad específica (ej: diabetes)

2. **Filtro de Spam**
   - Clases: "Spam" vs "No Spam"
   - Aplicación: Clasificar correos electrónicos entrantes

3. **Aprobación de Crédito**
   - Clases: "Aprobado" vs "Rechazado"
   - Aplicación: Decidir si otorgar un préstamo a un cliente

4. **Predicción de Abandono de Clientes (Churn)**
   - Clases: "Se quedará" vs "Se irá"
   - Aplicación: Identificar clientes en riesgo de cancelar un servicio

**Cuándo usar:**  
Cuando el problema tiene exactamente dos resultados posibles y necesitas una decisión clara entre dos opciones.

---

#### Clasificación Multiclase

**Definición:**  
La clasificación multiclase es cuando el modelo debe predecir entre **tres o más clases posibles**.

**Características:**
- Múltiples categorías (≥ 3)
- Una observación pertenece a una sola clase
- Más compleja que la clasificación binaria

**Ejemplos:**

1. **Reconocimiento de Dígitos Manuscritos**
   - Clases: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (10 clases)
   - Aplicación: Leer códigos postales o cheques bancarios

2. **Clasificación de Tipos de Flores**
   - Clases: "Iris Setosa", "Iris Versicolor", "Iris Virginica"
   - Aplicación: Identificar especies de plantas en botánica

3. **Categorización de Noticias**
   - Clases: "Deportes", "Política", "Tecnología", "Entretenimiento", "Economía"
   - Aplicación: Organizar automáticamente artículos en un portal de noticias

4. **Clasificación de Enfermedades**
   - Clases: Múltiples tipos de cáncer o condiciones médicas
   - Aplicación: Diagnóstico diferencial en medicina

**Cuándo usar:**  
Cuando el problema tiene tres o más categorías posibles y cada observación pertenece a exactamente una de ellas.

---

#### Diferencias Clave

| Aspecto | Clasificación Binaria | Clasificación Multiclase |
|---------|----------------------|--------------------------|
| **Número de clases** | 2 | ≥ 3 |
| **Complejidad** | Menor | Mayor |
| **Función de activación** | Sigmoid | Softmax |
| **Métrica común** | AUC-ROC | Accuracy, F1 macro/micro |
| **Ejemplo** | Spam vs No Spam | Clasificar animales en gato, perro, pájaro |

---

### 3. ¿Cuáles son los principales algoritmos de clasificación supervisada?

#### 🔹 Regresión Logística (Logistic Regression)

**Descripción:**  
A pesar de su nombre, la regresión logística es un algoritmo de **clasificación** que predice la probabilidad de que una observación pertenezca a una clase específica. Utiliza la función sigmoide para mapear las predicciones a valores entre 0 y 1.

**Funcionamiento:**
- Calcula una combinación lineal de las características
- Aplica la función logística (sigmoide): σ(z) = 1 / (1 + e^(-z))
- Si la probabilidad es > 0.5 → Clase 1, si no → Clase 0

**Características:**
- **Ventajas:**
  - Simple e interpretable
  - Rápido de entrenar
  - Proporciona probabilidades
  - Funciona bien con relaciones lineales
  - Pocos hiperparámetros
  
- **Desventajas:**
  - Asume linealidad entre características y log-odds
  - No captura relaciones no lineales complejas
  - Sensible a outliers

**Casos de uso ideales:**
- Clasificación binaria con relaciones lineales
- Cuando se necesita interpretar las probabilidades
- Baseline para comparar modelos más complejos
- Problemas con muchas características

**Ejemplo:** Predecir si un estudiante aprobará un examen basándose en horas de estudio.

---

#### 🔹 Árboles de Decisión (Decision Trees)

**Descripción:**  
Los árboles de decisión dividen el espacio de características mediante reglas if-then-else, creando una estructura jerárquica similar a un diagrama de flujo. Cada nodo interno representa una pregunta sobre una característica, y cada hoja representa una predicción de clase.

**Funcionamiento:**
1. Selecciona la mejor característica para dividir los datos (basándose en Gini o Entropía)
2. Crea ramas para cada valor posible de esa característica
3. Repite el proceso recursivamente para cada subconjunto
4. Se detiene cuando se alcanza un criterio (pureza, profundidad máxima, etc.)

**Criterios de división:**
- **Gini Impurity:** Mide la probabilidad de clasificar incorrectamente
- **Entropy (Información Gain):** Mide el desorden en los datos

**Características:**
- **Ventajas:**
  - Extremadamente interpretables (visualización clara)
  - No requiere normalización de datos
  - Maneja datos numéricos y categóricos
  - Captura relaciones no lineales
  - Identifica características importantes automáticamente
  
- **Desventajas:**
  - Propenso al **overfitting**
  - Inestable (pequeños cambios en datos → árbol diferente)
  - Puede crear árboles sesgados con clases desbalanceadas
  - Menor precisión comparado con ensemble methods

**Casos de uso ideales:**
- Cuando se necesita explicabilidad
- Problemas con características mixtas (numéricas y categóricas)
- Exploración inicial de datos
- Generar reglas de negocio interpretables

**Ejemplo:** Decidir si una familia adoptará una mascota basándose en tamaño de casa, tiempo libre y presencia de niños.

---

#### 🔹 Support Vector Machine (SVM)

**Descripción:**  
SVM busca el hiperplano óptimo que maximiza el margen entre las clases. El margen es la distancia entre el hiperplano y los puntos más cercanos de cada clase (vectores de soporte).

**Funcionamiento:**
1. Encuentra el hiperplano que separa las clases
2. Maximiza la distancia (margen) a los puntos más cercanos
3. Los puntos más cercanos se llaman "vectores de soporte"
4. Puede usar kernels para problemas no lineales

**Tipos de Kernels:**
- **Lineal:** Para datos linealmente separables
- **Polinómico:** Captura interacciones polinómicas
- **RBF (Radial Basis Function):** Para patrones complejos no lineales
- **Sigmoide:** Similar a redes neuronales

**Características:**
- **Ventajas:**
  - Efectivo en espacios de alta dimensionalidad
  - Robusto ante outliers (solo los vectores de soporte importan)
  - Versatilidad mediante kernels
  - Funciona bien con datos complejos no lineales
  - Eficiente en memoria (solo almacena vectores de soporte)
  
- **Desventajas:**
  - Costoso computacionalmente con grandes datasets
  - Difícil de interpretar (especialmente con kernels no lineales)
  - Sensible a la elección del kernel y parámetros
  - No proporciona estimaciones de probabilidad directamente
  - Requiere normalización de características

**Casos de uso ideales:**
- Clasificación de texto y reconocimiento de caracteres
- Clasificación de imágenes
- Datos con alta dimensionalidad
- Cuando hay un margen claro de separación

**Ejemplo:** Clasificar tipos de flores (Iris) basándose en longitud y anchura de pétalos.

---

#### 🔹 K-Nearest Neighbors (KNN)

**Descripción:**  
KNN es un algoritmo basado en instancias que clasifica nuevos puntos según las clases de sus k vecinos más cercanos. Es un método "lazy learning" porque no construye un modelo explícito, sino que almacena todos los datos de entrenamiento.

**Funcionamiento:**
1. Cuando llega un nuevo punto, calcula la distancia a todos los puntos de entrenamiento
2. Selecciona los K vecinos más cercanos
3. Realiza votación mayoritaria (clasificación) o promedio (regresión)
4. Asigna la clase más común entre los K vecinos

**Métricas de distancia:**
- **Euclidiana:** √(Σ(xi - yi)²) - más común
- **Manhattan:** Σ|xi - yi|
- **Minkowski:** Generalización de Euclidiana y Manhattan
- **Coseno:** Para similitud de textos

**Características:**
- **Ventajas:**
  - Simple de entender e implementar
  - No requiere entrenamiento (lazy learning)
  - Naturalmente multiclase
  - Se adapta a nuevos datos fácilmente
  - Efectivo para datos con fronteras no lineales
  
- **Desventajas:**
  - Lento en predicción con grandes datasets
  - Sensible a la escala de características (requiere normalización)
  - Sensible al ruido y outliers
  - Curse of dimensionality (mal rendimiento en alta dimensionalidad)
  - Requiere almacenar todos los datos de entrenamiento

**Selección de K:**
- K pequeño: Más sensible al ruido, fronteras complejas
- K grande: Más suave, puede ignorar patrones locales
- K óptimo: Se determina mediante validación cruzada

**Casos de uso ideales:**
- Sistemas de recomendación
- Clasificación de patrones simples
- Cuando los datos de entrenamiento son pequeños
- Reconocimiento de patrones locales

**Ejemplo:** Clasificar frutas (manzanas vs naranjas) basándose en peso y diámetro.

---

#### 🔹 Naive Bayes

**Descripción:**  
Naive Bayes es un clasificador probabilístico basado en el Teorema de Bayes. Asume independencia condicional entre las características (de ahí "naive" o ingenuo), lo que simplifica los cálculos.

**Teorema de Bayes:**
```
P(Clase|Características) = P(Características|Clase) × P(Clase) / P(Características)
```

**Funcionamiento:**
1. Calcula la probabilidad a priori de cada clase
2. Para cada clase, calcula la probabilidad de observar las características
3. Aplica el Teorema de Bayes
4. Asigna la clase con mayor probabilidad posterior

**Variantes:**
- **Gaussian Naive Bayes:** Para características continuas (asume distribución normal)
- **Multinomial Naive Bayes:** Para características discretas (conteos, frecuencias)
- **Bernoulli Naive Bayes:** Para características binarias

**Características:**
- **Ventajas:**
  - Extremadamente rápido en entrenamiento y predicción
  - Funciona bien con pocas muestras de entrenamiento
  - Excelente para clasificación de texto (spam filtering, sentiment analysis)
  - Maneja alta dimensionalidad eficientemente
  - Proporciona probabilidades de clase
  - Simple de implementar
  
- **Desventajas:**
  - Asunción de independencia raramente se cumple en realidad
  - No captura interacciones entre características
  - Puede ser superado por modelos más sofisticados
  - Sensible a características irrelevantes

**Casos de uso ideales:**
- Clasificación de texto (análisis de sentimiento, categorización de documentos)
- Filtrado de spam
- Diagnósticos médicos basados en síntomas
- Sistemas de recomendación simples
- Cuando se necesita velocidad y simplicidad

**Ejemplo:** Clasificar correos electrónicos como spam o no spam basándose en la frecuencia de palabras.

---

### 4. ¿Qué métricas se utilizan para evaluar modelos de clasificación?

Las métricas de evaluación son fundamentales para medir el rendimiento de un modelo de clasificación. La elección de la métrica depende del problema específico y del costo de los diferentes tipos de errores.

---

#### 📊 Accuracy (Exactitud)

**Definición:**  
Es la proporción de predicciones correctas sobre el total de predicciones realizadas.

**Fórmula:**
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)

Donde:
- TP (True Positives): Predicciones positivas correctas
- TN (True Negatives): Predicciones negativas correctas
- FP (False Positives): Predicciones positivas incorrectas (Error Tipo I)
- FN (False Negatives): Predicciones negativas incorrectas (Error Tipo II)
```

**Interpretación:**
- Valor entre 0 y 1 (o 0% a 100%)
- Accuracy = 1 significa predicciones perfectas
- Accuracy = 0.85 significa que el modelo acierta el 85% de las veces

**Ventajas:**
- Fácil de entender e interpretar
- Métrica intuitiva para comparar modelos
- Buena métrica general de rendimiento

**Desventajas y Limitaciones:**
- **Paradoja de la Accuracy con clases desbalanceadas:**
  
  **Ejemplo:** Dataset de fraude bancario
  - 9,900 transacciones legítimas (99%)
  - 100 transacciones fraudulentas (1%)
  
  Un modelo que prediga "todo es legítimo" tendría:
  - Accuracy = 99% ¡Pero no detecta ningún fraude!
  - Este modelo es inútil pero tiene alta accuracy

**Cuándo usar:**
- ✅ Cuando las clases están balanceadas
- ✅ Cuando todos los errores tienen el mismo costo
- ❌ NO usar con datasets desbalanceados
- ❌ NO usar cuando ciertos errores son más críticos que otros

---

#### 📊 Precision (Precisión)

**Definición:**  
De todas las predicciones positivas que hizo el modelo, ¿cuántas fueron realmente positivas?

**Fórmula:**
```
Precision = TP / (TP + FP)
```

**Pregunta que responde:**  
"¿Qué tan confiable es el modelo cuando predice la clase positiva?"

**Interpretación:**
- Precision = 1 significa que todas las predicciones positivas fueron correctas
- Precision = 0.8 significa que el 80% de las predicciones positivas fueron correctas
- Alta precisión → Pocos falsos positivos

**Ejemplo Práctico:**

**Problema:** Sistema de recomendación de películas
- TP: Películas recomendadas que al usuario le gustaron
- FP: Películas recomendadas que al usuario NO le gustaron

Alta precisión significa: "Cuando el sistema recomienda algo, probablemente te gustará"

**Cuándo priorizar Precision:**
- 🎯 Cuando los **falsos positivos son costosos**
- **Ejemplo 1 - Marketing:** Enviar emails promocionales solo a clientes realmente interesados (evitar molestar a usuarios)
- **Ejemplo 2 - Medicina:** Confirmar un diagnóstico grave antes de tratamiento invasivo
- **Ejemplo 3 - Sistema judicial:** Acusar a alguien de un crimen (mejor no acusar inocentes)
- **Ejemplo 4 - Spam filter:** Marcar emails como spam (no queremos que emails importantes vayan a spam)

---

#### 📊 Recall (Sensibilidad / Sensitivity / True Positive Rate)

**Definición:**  
De todos los casos realmente positivos, ¿cuántos detectó correctamente el modelo?

**Fórmula:**
```
Recall = TP / (TP + FN)
```

**Pregunta que responde:**  
"¿Qué tan bueno es el modelo para encontrar todos los casos positivos?"

**Interpretación:**
- Recall = 1 significa que el modelo encontró todos los casos positivos
- Recall = 0.8 significa que el modelo detectó el 80% de los casos positivos
- Alto recall → Pocos falsos negativos

**Ejemplo Práctico:**

**Problema:** Detección de tumores cancerígenos
- TP: Tumores cancerígenos detectados correctamente
- FN: Tumores cancerígenos NO detectados (ERROR GRAVE)

Alto recall significa: "El modelo no se pierde casos de cáncer"

**Cuándo priorizar Recall:**
- 🎯 Cuando los **falsos negativos son costosos**
- **Ejemplo 1 - Medicina:** Detección de enfermedades graves (no queremos perder ningún caso)
- **Ejemplo 2 - Seguridad:** Detección de fraude bancario (mejor alertar de más que perder un fraude)
- **Ejemplo 3 - Rescates:** Detectar personas en emergencias (no queremos dejar a nadie sin ayuda)
- **Ejemplo 4 - Control de calidad:** Detectar productos defectuosos (no queremos que salgan al mercado)

---

#### ⚖️ Trade-off entre Precision y Recall

Existe una tensión natural entre estas dos métricas:

**Aumentar Precision → Disminuye Recall**
- Ser más estricto en las predicciones positivas
- Menos falsos positivos, pero más falsos negativos

**Aumentar Recall → Disminuye Precision**
- Ser más permisivo en las predicciones positivas
- Menos falsos negativos, pero más falsos positivos

**Ejemplo visual:**
```
Sistema de detección de spam MUY ESTRICTO:
- Precision alta (poco spam legítimo marcado como spam)
- Recall bajo (algunos spams se cuelan como legítimos)

Sistema de detección de spam MUY PERMISIVO:
- Precision baja (muchos emails legítimos marcados como spam)
- Recall alto (casi todo el spam es detectado)
```

---

#### 📊 F1-Score

**Definición:**  
Es la media armónica entre Precision y Recall. Proporciona un balance entre ambas métricas.

**Fórmula:**
```
F1-Score = 2 × (Precision × Recall) / (Precision + Recall)
```

**¿Por qué media armónica y no media aritmética?**
- La media armónica penaliza valores extremos
- Si Precision o Recall es muy bajo, el F1-Score también será bajo
- Ejemplo: Precision=1.0, Recall=0.1
  - Media aritmética = 0.55 (engañosamente alto)
  - F1-Score = 0.18 (refleja el desequilibrio)

**Interpretación:**
- F1 = 1 es perfecto (precision y recall perfectos)
- F1 alto indica buen balance entre precision y recall
- F1 bajo indica que al menos una de las métricas es mala

**Variantes:**

**F-Beta Score:** Permite dar más peso a Precision o Recall
```
Fβ = (1 + β²) × (Precision × Recall) / (β² × Precision + Recall)

- β < 1: Mayor peso a Precision
- β > 1: Mayor peso a Recall
- β = 1: F1-Score (balance igual)
- β = 2: F2-Score (doble peso a Recall)
```

**Cuándo usar F1-Score:**
- ✅ Clases desbalanceadas
- ✅ Cuando necesitas balance entre Precision y Recall
- ✅ Cuando ambos tipos de errores son importantes
- ✅ Para comparar modelos de manera equilibrada

---

#### 📊 Matriz de Confusión (Confusion Matrix)

**Definición:**  
Es una tabla que visualiza el rendimiento de un modelo de clasificación mostrando las predicciones vs los valores reales.

**Estructura (Clasificación Binaria):**

```
                      Predicción
                   Negativo  Positivo
Real  Negativo  |    TN    |    FP    |
      Positivo  |    FN    |    TP    |
```

**Componentes:**
- **True Negatives (TN):** Correctamente predijo clase negativa
- **True Positives (TP):** Correctamente predijo clase positiva
- **False Positives (FP):** Predijo positivo pero era negativo (Error Tipo I)
- **False Negatives (FN):** Predijo negativo pero era positivo (Error Tipo II)

**Ejemplo Numérico:**

**Problema:** Detección de cáncer en 100 pacientes

```
                      Predicción
                   Sano    Enfermo
Real  Sano      |   85   |    5    | = 90 pacientes sanos
      Enfermo   |   2    |    8    | = 10 pacientes enfermos
                 ----------------------
                   87       13
```

**Cálculos:**
- **Accuracy** = (85 + 8) / 100 = 0.93 (93%)
- **Precision** = 8 / (8 + 5) = 0.615 (61.5%)
- **Recall** = 8 / (8 + 2) = 0.80 (80%)
- **F1-Score** = 2 × (0.615 × 0.80) / (0.615 + 0.80) = 0.696

**Interpretación:**
- 85 personas sanas correctamente identificadas ✅
- 8 personas enfermas correctamente identificadas ✅
- 5 personas sanas incorrectamente diagnosticadas como enfermas ⚠️ (tratamientos innecesarios)
- 2 personas enfermas NO detectadas ⛔ (¡MUY GRAVE!)

**Para Clasificación Multiclase:**

Ejemplo con 3 clases (Gato, Perro, Pájaro):

```
           Predicción
           Gato  Perro  Pájaro
Real Gato    45    3      2
     Perro    2   38      5
     Pájaro   1    4     40
```

**Ventajas de la Matriz de Confusión:**
- Visualización clara de dónde se equivoca el modelo
- Identifica patrones de confusión entre clases específicas
- Base para calcular todas las demás métricas
- Útil para clases múltiples

---

#### 📊 ROC-AUC (Receiver Operating Characteristic - Area Under Curve)

**ROC Curve (Curva ROC):**

**Definición:**  
Es una representación gráfica que muestra el rendimiento de un modelo de clasificación en todos los umbrales de decisión posibles.

**Ejes:**
- **Eje Y:** TPR (True Positive Rate) = Recall = TP / (TP + FN)
- **Eje X:** FPR (False Positive Rate) = FP / (FP + TN)

**Interpretación de la Curva:**
- Muestra el trade-off entre TPR (beneficio) y FPR (costo)
- Cada punto de la curva representa un umbral diferente
- Cuanto más cerca esté la curva de la esquina superior izquierda, mejor

**AUC (Area Under the Curve):**

**Definición:**  
Es el área bajo la curva ROC. Representa la probabilidad de que el modelo clasifique correctamente un ejemplo positivo aleatorio por encima de un ejemplo negativo aleatorio.

**Interpretación de valores:**
```
AUC = 1.0   → Modelo perfecto (clasificación perfecta)
AUC = 0.9-1.0 → Excelente
AUC = 0.8-0.9 → Muy bueno
AUC = 0.7-0.8 → Bueno
AUC = 0.6-0.7 → Regular
AUC = 0.5   → Modelo inútil (como lanzar una moneda)
AUC < 0.5   → Peor que aleatorio (predicciones invertidas)
```

**Ventajas de ROC-AUC:**
- **Independiente del umbral:** Evalúa el modelo en todos los umbrales posibles
- **Robusta ante clases desbalanceadas:** A diferencia de accuracy
- **Comparación de modelos:** Fácil de comparar varios modelos
- **Interpretación probabilística:** Mide capacidad discriminativa

**Desventajas:**
- Puede ser optimista con clases muy desbalanceadas
- No proporciona información sobre calibración de probabilidades
- Puede enmascarar problemas en clases específicas

**Cuándo usar ROC-AUC:**
- ✅ Comparar múltiples modelos
- ✅ Cuando no hay un umbral de decisión fijo
- ✅ Para evaluar modelos que producen probabilidades
- ✅ En clasificación binaria
- ⚠️ Con precaución en datasets muy desbalanceados (considerar Precision-Recall curve)

**Alternativa para clases desbalanceadas:**
**PR-AUC (Precision-Recall AUC):** Más informativa cuando la clase positiva es rara

---

#### 📊 Resumen Comparativo de Métricas

| Métrica | Cuándo Usar | Ventaja Principal | Limitación Principal |
|---------|-------------|-------------------|----------------------|
| **Accuracy** | Clases balanceadas | Fácil interpretación | Engañosa con desbalance |
| **Precision** | Evitar FP costosos | Minimiza falsos positivos | Ignora FN |
| **Recall** | Evitar FN costosos | Minimiza falsos negativos | Ignora FP |
| **F1-Score** | Balance FP y FN | Combina Precision y Recall | Puede enmascarar debilidades |
| **Confusion Matrix** | Análisis detallado | Visualiza todos los errores | No es un número único |
| **ROC-AUC** | Comparar modelos | Independiente umbral | Optimista con desbalance |

---

### 5. ¿Qué es el feature engineering y feature selection en clasificación?

#### 🔧 Feature Engineering (Ingeniería de Características)

**Definición:**  
Feature Engineering es el proceso de crear nuevas características (features) o transformar las existentes para mejorar el rendimiento del modelo de Machine Learning. Es considerado uno de los aspectos más importantes y creativos del ML.

**Objetivo:**
Extraer información más relevante de los datos crudos para que el modelo pueda aprender patrones más fácilmente.

---

##### **Técnicas Comunes de Feature Engineering**

**1. Creación de Características Numéricas:**

**a) Transformaciones Matemáticas:**
```python
# De datos crudos a características útiles
df['area'] = df['largo'] * df['ancho']
df['IMC'] = df['peso'] / (df['altura'] ** 2)
df['ratio_precio_superficie'] = df['precio'] / df['metros_cuadrados']
df['log_ingreso'] = np.log(df['ingreso'] + 1)
df['sqrt_edad'] = np.sqrt(df['edad'])
```

**Ejemplo Real - Ventas:**
```python
# Datos originales: ventas_mes, clientes_mes
# Características creadas:
df['venta_promedio_por_cliente'] = df['ventas_mes'] / df['clientes_mes']
df['crecimiento_ventas'] = df['ventas_mes'] - df['ventas_mes_anterior']
df['tasa_crecimiento'] = (df['ventas_mes'] / df['ventas_mes_anterior']) - 1
```

**b) Características Temporales:**
```python
# De datetime a múltiples características
df['fecha'] = pd.to_datetime(df['fecha'])
df['año'] = df['fecha'].dt.year
df['mes'] = df['fecha'].dt.month
df['dia_semana'] = df['fecha'].dt.dayofweek
df['dia_mes'] = df['fecha'].dt.day
df['trimestre'] = df['fecha'].dt.quarter
df['es_fin_de_semana'] = df['dia_semana'].isin([5, 6]).astype(int)
df['es_festivo'] = df['fecha'].isin(dias_festivos).astype(int)
df['hora_del_dia'] = df['fecha'].dt.hour
df['periodo_dia'] = pd.cut(df['hora_del_dia'], bins=[0,6,12,18,24], 
                           labels=['madrugada','mañana','tarde','noche'])
```

**Ejemplo Real - E-commerce:**
```python
# Predecir compras en una tienda online
df['dias_desde_ultima_compra'] = (fecha_actual - df['fecha_ultima_compra']).dt.days
df['dias_desde_registro'] = (fecha_actual - df['fecha_registro']).dt.days
df['compras_por_mes_actividad'] = df['total_compras'] / (df['dias_desde_registro'] / 30)
```

**c) Agregaciones:**
```python
# Características agregadas por grupo
clientes_agg = transacciones.groupby('cliente_id').agg({
    'monto': ['sum', 'mean', 'std', 'min', 'max'],
    'transaccion_id': 'count',
    'fecha': ['min', 'max']
}).reset_index()

clientes_agg.columns = ['cliente_id', 'monto_total', 'monto_promedio',
                        'monto_std', 'monto_min', 'monto_max',
                        'num_transacciones', 'primera_transaccion', 
                        'ultima_transaccion']
```

**2. Encoding de Variables Categóricas:**

**a) One-Hot Encoding:**
```python
# Para categorías nominales sin orden
# Original: ['Rojo', 'Verde', 'Azul']
# Resultado:
#   color_Rojo  color_Verde  color_Azul
#      1           0            0
#      0           1            0
#      0           0            1

pd.get_dummies(df, columns=['color'], drop_first=True)
```

**b) Label Encoding:**
```python
# Para categorías ordinales con orden
# Educación: ['Primaria', 'Secundaria', 'Universidad', 'Posgrado']
educacion_map = {
    'Primaria': 1,
    'Secundaria': 2,
    'Universidad': 3,
    'Posgrado': 4
}
df['educacion_encoded'] = df['educacion'].map(educacion_map)
```

**c) Target Encoding:**
```python
# Codificar basándose en la variable objetivo
# Útil para categorías con alta cardinalidad
ciudad_target_mean = df.groupby('ciudad')['compra'].mean()
df['ciudad_encoded'] = df['ciudad'].map(ciudad_target_mean)
```

**d) Frequency Encoding:**
```python
# Codificar por frecuencia de aparición
freq = df['marca'].value_counts(normalize=True)
df['marca_freq'] = df['marca'].map(freq)
```

**3. Binning (Discretización):**
```python
# Convertir variables continuas en categóricas
df['edad_grupo'] = pd.cut(df['edad'], 
                          bins=[0, 18, 35, 50, 65, 100],
                          labels=['Menor', 'Joven', 'Adulto', 'Senior', 'Anciano'])

df['ingreso_nivel'] = pd.qcut(df['ingreso'], 
                               q=4, 
                               labels=['Bajo', 'Medio-Bajo', 'Medio-Alto', 'Alto'])
```

**4. Interacciones entre Características:**
```python
# Crear características combinadas
df['edad_x_ingreso'] = df['edad'] * df['ingreso']
df['area_x_habitaciones'] = df['area'] * df['habitaciones']

# Interacciones polinómicas
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
features_poly = poly.fit_transform(df[['feature1', 'feature2']])
```

**5. Características de Texto:**

```python
# De texto crudo a características numéricas
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Bag of Words
vectorizer = CountVectorizer(max_features=1000)
bow_features = vectorizer.fit_transform(df['texto'])

# TF-IDF
tfidf = TfidfVectorizer(max_features=1000, ngram_range=(1,2))
tfidf_features = tfidf.fit_transform(df['texto'])

# Características adicionales
df['longitud_texto'] = df['texto'].str.len()
df['num_palabras'] = df['texto'].str.split().str.len()
df['num_mayusculas'] = df['texto'].str.count('[A-Z]')
df['num_signos_exclamacion'] = df['texto'].str.count('!')
df['tiene_url'] = df['texto'].str.contains('http').astype(int)
```

**6. Scaling y Normalización:**
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# StandardScaler: media=0, std=1
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[numeric_features])

# MinMaxScaler: rango [0,1]
scaler = MinMaxScaler()
df_normalized = scaler.fit_transform(df[numeric_features])

# RobustScaler: robusto a outliers
scaler = RobustScaler()
df_robust = scaler.fit_transform(df[numeric_features])
```

---

##### **Importancia del Feature Engineering**

**Impacto en el Rendimiento:**
> "Coming up with features is difficult, time-consuming, requires expert knowledge. 
> Applied machine learning is basically feature engineering." 
> — Andrew Ng

**Estadísticas:**
- Puede mejorar la accuracy de 70% a 95% en algunos problemas
- Modelos simples con buenas características > Modelos complejos con características malas
- 80% del tiempo en ML se gasta en feature engineering

**Ejemplo Real:**

**Problema:** Predecir cancelación de suscripciones (Churn)

**Características Originales:**
- fecha_registro, fecha_ultima_visita, num_compras, monto_total

**Features Engineered:**
```python
# Mucho más poderosas:
- dias_inactivo = (hoy - fecha_ultima_visita).days
- frecuencia_compras = num_compras / meses_activo
- ticket_promedio = monto_total / num_compras
- tendencia_compras = (compras_ultimos_3_meses - compras_3_meses_anteriores)
- ratio_productos_premium = compras_premium / num_compras
- engagement_score = visitas_mes * (compras_mes / visitas_mes)
```

**Resultado:** Accuracy aumentó de 72% a 89%

---

#### 🎯 Feature Selection (Selección de Características)

**Definición:**  
Feature Selection es el proceso de seleccionar el subconjunto más relevante de características que contribuyen significativamente a la predicción, eliminando características redundantes o irrelevantes.

**¿Por qué es importante?**

**Problemas con demasiadas características:**
- **Overfitting:** El modelo memoriza ruido
- **Curse of Dimensionality:** Rendimiento degradado en alta dimensionalidad
- **Mayor tiempo de entrenamiento:** Más características = más lento
- **Dificultad de interpretación:** Modelos complejos difíciles de explicar
- **Correlaciones espurias:** Características irrelevantes que parecen útiles por azar

**Beneficios de Feature Selection:**
- ✅ Mejora la generalización del modelo
- ✅ Reduce overfitting
- ✅ Acelera el entrenamiento
- ✅ Mejora la interpretabilidad
- ✅ Reduce ruido

---

##### **Métodos de Feature Selection**

**1. Filter Methods (Métodos de Filtro)**

**Característica:** Independientes del modelo, usan estadísticas.

**a) Correlación:**
```python
# Eliminar características con alta correlación entre sí
correlation_matrix = df.corr()

# Encontrar pares altamente correlacionados
high_corr = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > 0.9:
            high_corr.append(correlation_matrix.columns[i])

# Eliminar características redundantes
df_reduced = df.drop(columns=high_corr)
```

**b) Chi-Squared Test:**
```python
from sklearn.feature_selection import SelectKBest, chi2

# Para características categóricas
selector = SelectKBest(chi2, k=10)  # Seleccionar top 10
X_selected = selector.fit_transform(X, y)
selected_features = X.columns[selector.get_support()]
```

**c) Variance Threshold:**
```python
from sklearn.feature_selection import VarianceThreshold

# Eliminar características con baja varianza
selector = VarianceThreshold(threshold=0.1)
X_high_variance = selector.fit_transform(X)
```

**d) Mutual Information:**
```python
from sklearn.feature_selection import mutual_info_classif

# Mide dependencia no lineal con variable objetivo
mi_scores = mutual_info_classif(X, y)
mi_scores = pd.Series(mi_scores, index=X.columns)
mi_scores.sort_values(ascending=False)
```

**2. Wrapper Methods (Métodos de Envoltura)**

**Característica:** Usan el modelo para evaluar subconjuntos de características.

**a) Forward Selection:**
```python
# Agregar características una por una
def forward_selection(X, y, model):
    selected_features = []
    remaining_features = list(X.columns)
    
    while remaining_features:
        best_score = 0
        best_feature = None
        
        for feature in remaining_features:
            test_features = selected_features + [feature]
            X_test = X[test_features]
            score = cross_val_score(model, X_test, y, cv=5).mean()
            
            if score > best_score:
                best_score = score
                best_feature = feature
        
        if best_feature:
            selected_features.append(best_feature)
            remaining_features.remove(best_feature)
        else:
            break
    
    return selected_features
```

**b) Backward Elimination:**
```python
# Eliminar características una por una
def backward_elimination(X, y, model, threshold=0.01):
    features = list(X.columns)
    
    while len(features) > 1:
        X_subset = X[features]
        scores = cross_val_score(model, X_subset, y, cv=5)
        baseline_score = scores.mean()
        
        worst_feature = None
        smallest_drop = threshold
        
        for feature in features:
            test_features = [f for f in features if f != feature]
            X_test = X[test_features]
            score = cross_val_score(model, X_test, y, cv=5).mean()
            drop = baseline_score - score
            
            if drop < smallest_drop:
                smallest_drop = drop
                worst_feature = feature
        
        if worst_feature:
            features.remove(worst_feature)
        else:
            break
    
    return features
```

**c) Recursive Feature Elimination (RFE):**
```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
rfe = RFE(estimator=model, n_features_to_select=10)
rfe.fit(X, y)

selected_features = X.columns[rfe.support_]
feature_ranking = pd.Series(rfe.ranking_, index=X.columns)
```

**3. Embedded Methods (Métodos Embebidos)**

**Característica:** La selección de características es parte del entrenamiento del modelo.

**a) Lasso (L1 Regularization):**
```python
from sklearn.linear_model import LassoCV

# Lasso elimina características poniendo coeficientes en 0
lasso = LassoCV(cv=5)
lasso.fit(X, y)

# Características seleccionadas (coeficientes no cero)
selected_features = X.columns[lasso.coef_ != 0]
```

**b) Feature Importance (Random Forest, XGBoost):**
```python
from sklearn.ensemble import RandomForestClassifier

# Entrenar modelo
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X, y)

# Obtener importancia
feature_importance = pd.Series(rf.feature_importances_, index=X.columns)
feature_importance = feature_importance.sort_values(ascending=False)

# Seleccionar top N características
top_features = feature_importance.head(15).index
X_selected = X[top_features]
```

**c) XGBoost Feature Importance:**
```python
import xgboost as xgb

model = xgb.XGBClassifier()
model.fit(X, y)

# Múltiples tipos de importancia
xgb.plot_importance(model, importance_type='weight')  # Frecuencia de uso
xgb.plot_importance(model, importance_type='gain')    # Ganancia promedio
xgb.plot_importance(model, importance_type='cover')   # Cobertura promedio
```

---

##### **Comparación de Métodos**

| Método | Velocidad | Accuracy | Interpretabilidad | Cuándo Usar |
|--------|-----------|----------|-------------------|-------------|
| **Filter** | Muy rápido | Buena | Alta | Datasets grandes, análisis exploratorio |
| **Wrapper** | Lento | Mejor | Media | Datasets pequeños/medianos, máximo rendimiento |
| **Embedded** | Rápido | Muy buena | Alta | Balance velocidad-rendimiento, modelos con regularización |

---

##### **Estrategia Recomendada**

**Pipeline Completo:**

```python
# 1. Análisis Exploratorio
- Identificar características con missing values
- Analizar distribuciones
- Detectar outliers

# 2. Feature Engineering
- Crear características derivadas
- Encoding de categóricas
- Scaling/normalización

# 3. Feature Selection - Fase 1 (Filter)
- Eliminar características con varianza cero
- Eliminar características altamente correlacionadas
- Calcular mutual information

# 4. Feature Selection - Fase 2 (Embedded)
- Entrenar Random Forest o XGBoost
- Seleccionar por feature importance

# 5. Feature Selection - Fase 3 (Wrapper - opcional)
- RFE para refinar selección
- Validar con cross-validation

# 6. Evaluación Final
- Comparar rendimiento con todas las características vs seleccionadas
- Analizar trade-offs interpretabilidad-rendimiento
```

**Ejemplo Completo:**

```python
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold, SelectKBest, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# 1. Feature Engineering
df['edad_al_cuadrado'] = df['edad'] ** 2
df['ingreso_log'] = np.log1p(df['ingreso'])
df['ratio_deuda_ingreso'] = df['deuda'] / df['ingreso']

# 2. Encoding
df_encoded = pd.get_dummies(df, columns=['ciudad', 'profesion'])

# 3. Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Remove low variance
var_selector = VarianceThreshold(threshold=0.1)
X_high_var = var_selector.fit_transform(X_scaled)

# 5. Mutual Information
mi_selector = SelectKBest(mutual_info_classif, k=20)
X_mi = mi_selector.fit_transform(X_high_var, y)

# 6. Feature Importance
rf = RandomForestClassifier()
rf.fit(X_mi, y)
importances = pd.Series(rf.feature_importances_)
top_features = importances.nlargest(15).index

# 7. Evaluación
X_final = X_mi[:, top_features]
score = cross_val_score(rf, X_final, y, cv=5).mean()
print(f"Score con {len(top_features)} características: {score:.4f}")
```

---

### 7. ¿Qué son los hiperparámetros y cómo se optimizan/ajustan?

#### 🎛️ Hiperparámetros

**Definición:**  
Los hiperparámetros son configuraciones o ajustes que se establecen **antes** de entrenar un modelo de Machine Learning. A diferencia de los parámetros (que el modelo aprende durante el entrenamiento), los hiperparámetros se deben definir de antemano y controlan el proceso de aprendizaje.

---

##### **Diferencia: Parámetros vs Hiperparámetros**

| Aspecto | Parámetros | Hiperparámetros |
|---------|------------|-----------------|
| **Definición** | Valores que el modelo aprende de los datos | Valores que configuran el proceso de aprendizaje |
| **Cuándo se determinan** | Durante el entrenamiento | Antes del entrenamiento |
| **Ejemplo (Reg. Lineal)** | Coeficientes (weights), intercepto | Learning rate, regularización |
| **Ejemplo (Decision Tree)** | Reglas de división aprendidas | max_depth, min_samples_split |
| **Ejemplo (Neural Network)** | Pesos de las conexiones | Número de capas, neuronas, learning rate |
| **Cómo se obtienen** | Optimización automática (gradiente descendente) | Búsqueda manual o automática |

---

##### **Ejemplos de Hiperparámetros por Algoritmo**

**1. Regresión Logística:**
```python
LogisticRegression(
    C=1.0,                    # Inverso de regularización (menor C = más regularización)
    penalty='l2',             # Tipo de regularización: 'l1', 'l2', 'elasticnet'
    solver='lbfgs',           # Algoritmo de optimización
    max_iter=100,             # Número máximo de iteraciones
    class_weight='balanced'   # Manejo de clases desbalanceadas
)
```

**2. Random Forest:**
```python
RandomForestClassifier(
    n_estimators=100,         # Número de árboles
    max_depth=None,           # Profundidad máxima de árboles
    min_samples_split=2,      # Mínimo de muestras para dividir nodo
    min_samples_leaf=1,       # Mínimo de muestras en hoja
    max_features='sqrt',      # Número de características por split
    bootstrap=True,           # Usar bootstrap samples
    criterion='gini'          # Criterio de división: 'gini' o 'entropy'
)
```

**3. Support Vector Machine:**
```python
SVC(
    C=1.0,                    # Parámetro de regularización
    kernel='rbf',             # Tipo de kernel: 'linear', 'poly', 'rbf', 'sigmoid'
    gamma='scale',            # Coeficiente del kernel
    degree=3,                 # Grado del kernel polinómico
    class_weight='balanced'   # Balance de clases
)
```

**4. K-Nearest Neighbors:**
```python
KNeighborsClassifier(
    n_neighbors=5,            # Número de vecinos
    weights='uniform',        # Función de peso: 'uniform' o 'distance'
    metric='minkowski',       # Métrica de distancia
    p=2                       # Parámetro de Minkowski (2 = Euclidiana)
)
```

**5. XGBoost:**
```python
XGBClassifier(
    n_estimators=100,         # Número de árboles
    max_depth=6,              # Profundidad máxima
    learning_rate=0.1,        # Tasa de aprendizaje
    subsample=0.8,            # Fracción de muestras por árbol
    colsample_bytree=0.8,     # Fracción de características por árbol
    gamma=0,                  # Reducción de pérdida mínima para split
    reg_alpha=0,              # Regularización L1
    reg_lambda=1              # Regularización L2
)
```

---

#### 🔍 Optimización de Hiperparámetros (Hyperparameter Tuning)

**Objetivo:**  
Encontrar la combinación de hiperparámetros que maximiza el rendimiento del modelo en datos no vistos.

---

##### **1. Grid Search (Búsqueda en Cuadrícula)**

**Definición:**  
Prueba exhaustivamente todas las combinaciones posibles de hiperparámetros en una cuadrícula predefinida.

**Cómo funciona:**
1. Defines un grid (cuadrícula) con valores para cada hiperparámetro
2. El algoritmo prueba TODAS las combinaciones
3. Evalúa cada combinación con validación cruzada
4. Selecciona la mejor combinación

**Implementación en Python:**

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# 1. Definir el modelo
model = RandomForestClassifier(random_state=42)

# 2. Definir el grid de hiperparámetros
param_grid = {
    'n_estimators': [50, 100, 200],           # 3 opciones
    'max_depth': [10, 20, 30, None],          # 4 opciones
    'min_samples_split': [2, 5, 10],          # 3 opciones
    'min_samples_leaf': [1, 2, 4],            # 3 opciones
    'max_features': ['sqrt', 'log2']          # 2 opciones
}
# Total combinaciones: 3 × 4 × 3 × 3 × 2 = 216 combinaciones

# 3. Configurar GridSearchCV
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,                        # Validación cruzada de 5 folds
    scoring='accuracy',          # Métrica a optimizar
    n_jobs=-1,                   # Usar todos los cores disponibles
    verbose=2                    # Mostrar progreso
)

# 4. Ejecutar búsqueda
grid_search.fit(X_train, y_train)

# 5. Resultados
print("Mejores hiperparámetros:", grid_search.best_params_)
print("Mejor score:", grid_search.best_score_)
print("Mejor modelo:", grid_search.best_estimator_)

# 6. Usar el mejor modelo
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# 7. Ver todos los resultados
results = pd.DataFrame(grid_search.cv_results_)
results.sort_values('rank_test_score').head(10)
```

**Ejemplo Completo con XGBoost:**

```python
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

# Grid más complejo
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.3],
    'subsample': [0.7, 0.8, 0.9],
    'colsample_bytree': [0.7, 0.8, 0.9],
    'gamma': [0, 0.1, 0.2]
}

xgb_model = XGBClassifier(random_state=42)

grid_search = GridSearchCV(
    estimator=xgb_model,
    param_grid=param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1,
    verbose=2
)

grid_search.fit(X_train, y_train)

print(f"Mejores parámetros: {grid_search.best_params_}")
print(f"Mejor F1-Score: {grid_search.best_score_:.4f}")
```

**Ventajas de Grid Search:**
- ✅ Garantiza encontrar la mejor combinación dentro del grid
- ✅ Exhaustivo y sistemático
- ✅ Fácil de entender e implementar
- ✅ Reproducible

**Desventajas de Grid Search:**
- ❌ **Computacionalmente costoso** (crece exponencialmente)
- ❌ Puede tardar horas o días con grids grandes
- ❌ No escala bien con muchos hiperparámetros
- ❌ Puede desperdiciar recursos en zonas no prometedoras

**Cuándo usar Grid Search:**
- Pocos hiperparámetros (2-4)
- Grid pequeño
- Recursos computacionales disponibles
- Necesitas exploración exhaustiva

---

##### **2. Random Search (Búsqueda Aleatoria)**

**Definición:**  
En lugar de probar todas las combinaciones, Random Search muestrea aleatoriamente un número fijo de combinaciones de hiperparámetros.

**Ventaja clave:**  
Estudios muestran que Random Search puede encontrar configuraciones igual de buenas que Grid Search en **mucho menos tiempo**.

**¿Por qué funciona?**

**Teoría (Bergstra & Bengio, 2012):**
- No todos los hiperparámetros son igualmente importantes
- Random Search explora más valores para los hiperparámetros importantes
- Grid Search desperdicia evaluaciones en combinaciones similares

**Visualización conceptual:**
```
Grid Search (9 evaluaciones):
Hiperparámetro 1: [A, A, A, B, B, B, C, C, C]
Hiperparámetro 2: [X, Y, Z, X, Y, Z, X, Y, Z]

Random Search (9 evaluaciones):
Hiperparámetro 1: [A, D, B, F, C, E, A, G, H]  ← Más diversidad
Hiperparámetro 2: [X, W, Z, Y, T, V, S, U, R]  ← Más exploración
```

**Implementación en Python:**

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform
import numpy as np

# 1. Definir distribuciones de hiperparámetros
param_distributions = {
    'n_estimators': randint(50, 500),              # Enteros entre 50-500
    'max_depth': randint(3, 20),                   # Enteros entre 3-20
    'learning_rate': uniform(0.01, 0.3),           # Flotantes entre 0.01-0.31
    'subsample': uniform(0.5, 0.5),                # Flotantes entre 0.5-1.0
    'colsample_bytree': uniform(0.5, 0.5),         # Flotantes entre 0.5-1.0
    'gamma': uniform(0, 0.5),                      # Flotantes entre 0-0.5
    'min_child_weight': randint(1, 10),            # Enteros entre 1-10
    'reg_alpha': uniform(0, 1),                    # L1 regularization
    'reg_lambda': uniform(0, 1)                    # L2 regularization
}

# 2. Configurar RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=XGBClassifier(random_state=42),
    param_distributions=param_distributions,
    n_iter=100,                  # Número de combinaciones a probar
    cv=5,
    scoring='roc_auc',
    n_jobs=-1,
    verbose=2,
    random_state=42
)

# 3. Ejecutar búsqueda
random_search.fit(X_train, y_train)

# 4. Resultados
print("Mejores hiperparámetros:", random_search.best_params_)
print("Mejor AUC:", random_search.best_score_)

# 5. Comparar top 10 configuraciones
results = pd.DataFrame(random_search.cv_results_)
top_10 = results.sort_values('rank_test_score').head(10)
print(top_10[['params', 'mean_test_score', 'std_test_score']])
```

**Ejemplo con Random Forest:**

```python
from sklearn.ensemble import RandomForestClassifier

param_distributions = {
    'n_estimators': randint(100, 1000),
    'max_depth': [None] + list(randint(10, 100).rvs(10)),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'max_features': ['sqrt', 'log2', None],
    'bootstrap': [True, False],
    'criterion': ['gini', 'entropy']
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions=param_distributions,
    n_iter=50,
    cv=5,
    scoring='f1_weighted',
    n_jobs=-1,
    random_state=42
)

random_search.fit(X_train, y_train)
```

**Ventajas de Random Search:**
- ✅ **Mucho más rápido** que Grid Search
- ✅ Escala mejor con muchos hiperparámetros
- ✅ Explora más diversidad de valores
- ✅ Efectivo con presupuesto computacional limitado
- ✅ Puede encontrar combinaciones inesperadas

**Desventajas de Random Search:**
- ❌ No garantiza encontrar el óptimo global
- ❌ Puede requerir muchas iteraciones
- ❌ Aleatoriedad puede dar resultados inconsistentes

**Cuándo usar Random Search:**
- Muchos hiperparámetros (>4)
- Espacio de búsqueda grande
- Recursos computacionales limitados
- Exploración inicial

---

##### **3. Grid Search vs Random Search: Comparación**

| Aspecto | Grid Search | Random Search |
|---------|-------------|---------------|
| **Método** | Exhaustivo | Muestreo aleatorio |
| **Complejidad** | Exponencial | Lineal |
| **Tiempo** | Muy alto con muchos params | Controlable (n_iter) |
| **Cobertura** | Todos los valores predefinidos | Muestreo amplio del espacio |
| **Óptimo** | Garantizado en el grid | No garantizado |
| **Escalabilidad** | Mala | Buena |
| **Mejor para** | Pocos hiperparámetros | Muchos hiperparámetros |

**Recomendación práctica:**

```python
# Estrategia combinada:

# 1. Random Search amplio (exploración)
random_search = RandomizedSearchCV(
    model,
    param_distributions=wide_distributions,
    n_iter=100,
    cv=5
)
random_search.fit(X_train, y_train)

# 2. Grid Search refinado (explotación)
# Usar los mejores valores encontrados como centro
best_params = random_search.best_params_

refined_grid = {
    'n_estimators': [best_params['n_estimators']-50, 
                     best_params['n_estimators'],
                     best_params['n_estimators']+50],
    'max_depth': [best_params['max_depth']-2,
                  best_params['max_depth'],
                  best_params['max_depth']+2],
    # ... refinar otros parámetros
}

grid_search = GridSearchCV(model, refined_grid, cv=5)
grid_search.fit(X_train, y_train)

final_model = grid_search.best_estimator_
```

---

##### **4. Otras Técnicas Avanzadas de Optimización**

**Bayesian Optimization:**
```python
from skopt import BayesSearchCV
from skopt.space import Real, Integer

# Usa modelos probabilísticos para guiar la búsqueda
search_spaces = {
    'n_estimators': Integer(50, 500),
    'max_depth': Integer(3, 20),
    'learning_rate': Real(0.01, 0.3, prior='log-uniform'),
    'subsample': Real(0.5, 1.0),
}

bayes_search = BayesSearchCV(
    XGBClassifier(),
    search_spaces,
    n_iter=50,
    cv=5,
    n_jobs=-1
)
```

**Hyperband / ASHA:**
- Asignación dinámica de recursos
- Detiene configuraciones poco prometedoras temprano

**Optuna:**
```python
import optuna

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 500),
        'max_depth': trial.suggest_int('max_depth', 3, 20),
        'learning_rate': trial.suggest_loguniform('learning_rate', 0.01, 0.3),
    }
    
    model = XGBClassifier(**params)
    score = cross_val_score(model, X_train, y_train, cv=5).mean()
    return score

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

print('Best params:', study.best_params)
```

---

##### **5. Mejores Prácticas en Hyperparameter Tuning**

**✅ DO (Hacer):**

1. **Usa validación cruzada:**
   ```python
   GridSearchCV(cv=5)  # Siempre usar CV
   ```

2. **Separa test set:**
   ```python
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
   # Hacer tuning solo en X_train
   # Evaluar solo una vez en X_test al final
   ```

3. **Escala apropiadamente:**
   ```python
   # Incluir scaling en el pipeline
   from sklearn.pipeline import Pipeline
   
   pipeline = Pipeline([
       ('scaler', StandardScaler()),
       ('model', RandomForestClassifier())
   ])
   
   param_grid = {
       'model__n_estimators': [100, 200],
       'model__max_depth': [10, 20]
   }
   ```

4. **Empieza con rangos amplios:**
   ```python
   # Primera iteración: amplio
   param_grid_wide = {
       'learning_rate': [0.001, 0.01, 0.1, 1.0]
   }
   
   # Segunda iteración: refinado
   param_grid_refined = {
       'learning_rate': [0.08, 0.1, 0.12]
   }
   ```

5. **Monitorea tiempo de ejecución:**
   ```python
   import time
   
   start = time.time()
   grid_search.fit(X_train, y_train)
   print(f"Tiempo: {time.time() - start:.2f}s")
   ```

**❌ DON'T (No hacer):**

1. ❌ No hacer overfitting en test set
2. ❌ No optimizar en todo el dataset
3. ❌ No ignorar el tiempo de entrenamiento
4. ❌ No usar demasiados hiperparámetros simultáneamente
5. ❌ No olvidar el random_state para reproducibilidad

---

##### **Ejemplo Completo de Flujo de Trabajo:**

```python
from sklearn.model_selection import train_test_split, RandomizedSearchCV, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# 1. Split datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Random Search inicial (exploración amplia)
param_dist_wide = {
    'n_estimators': randint(50, 500),
    'max_depth': randint(5, 50),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'max_features': ['sqrt', 'log2', None]
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions=param_dist_wide,
    n_iter=50,
    cv=5,
    scoring='f1_weighted',
    n_jobs=-1,
    verbose=1,
    random_state=42
)

random_search.fit(X_train, y_train)
print(f"Mejor score Random Search: {random_search.best_score_:.4f}")
print(f"Mejores params: {random_search.best_params_}")

# 3. Grid Search refinado (explotación local)
best_params = random_search.best_params_

param_grid_refined = {
    'n_estimators': [best_params['n_estimators']-50,
                     best_params['n_estimators'],
                     best_params['n_estimators']+50],
    'max_depth': [best_params['max_depth']-5,
                  best_params['max_depth'],
                  best_params['max_depth']+5],
    'min_samples_split': [max(2, best_params['min_samples_split']-2),
                          best_params['min_samples_split'],
                          best_params['min_samples_split']+2],
    'max_features': [best_params['max_features']]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid=param_grid_refined,
    cv=5,
    scoring='f1_weighted',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)
print(f"Mejor score Grid Search: {grid_search.best_score_:.4f}")

# 4. Evaluación final en test set
final_model = grid_search.best_estimator_
y_pred = final_model.predict(X_test)

print("\nResultados en Test Set:")
print(classification_report(y_test, y_pred))
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

# 5. Guardar modelo
import joblib
joblib.dump(final_model, 'best_model.pkl')
```

---

## 📚 Conclusión

La clasificación en Machine Learning es un campo fundamental que requiere comprender:

1. **Los algoritmos** y cuándo usar cada uno
2. **Las métricas** apropiadas para evaluar el rendimiento
3. **Feature engineering** para extraer información valiosa
4. **Feature selection** para mantener solo lo relevante
5. **Optimización de hiperparámetros** para maximizar el rendimiento

El éxito en Machine Learning viene de:
- Entender profundamente el problema de negocio
- Experimentar con múltiples enfoques
- Validar rigurosamente los resultados
- Iterar y mejorar continuamente

---

## 📖 Referencias y Recursos Adicionales

### Documentación Oficial
- [Scikit-Learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Keras Documentation](https://keras.io/)

### Libros Recomendados
- "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" - Aurélien Géron
- "Pattern Recognition and Machine Learning" - Christopher Bishop
- "The Elements of Statistical Learning" - Hastie, Tibshirani, Friedman

### Cursos Online
- [Coursera: Machine Learning - Andrew Ng](https://www.coursera.org/learn/machine-learning)
- [Fast.ai: Practical Deep Learning](https://www.fast.ai/)
- [Google: Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

### Papers Importantes
- Bergstra & Bengio (2012): "Random Search for Hyper-Parameter Optimization"
- Breiman (2001): "Random Forests"
- Cortes & Vapnik (1995): "Support-Vector Networks"

---

**Fin del Documento**

