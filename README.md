# 🧠 Funciones de Activación en Machine Learning

## ✍️ Autor: **Demian Mundo**  
## 📅 Fecha: 22 de febrero de 2025  

---

## 🚀 Introducción  
Este proyecto consiste en graficar funciones de activación utilizando Python. Se han implementado 8 tipos diferentes de funciones de activación.

Las funciones de activación son fundamentales en las redes neuronales, ya que introducen no linealidad en el modelo y permiten que aprenda patrones complejos. Existen diversas funciones de activación, cada una con una aplicación específica dentro del Machine Learning.

Además, se incluye una pequeña guía para clonar este repositorio en su computadora.

---

## 🎯 Objetivo  
- Conocer y entender algunas funciones de activación utilizadas en el aprendizaje de máquina.  
- Graficar y visualizar estas funciones con Python.  
- Facilitar la reutilización del código mediante un repositorio organizado y modular.  

---

## 🔍 Importancia de las funciones de activación  
Las funciones de activación determinan la salida de una neurona, introducen no linealidad y facilitan el aprendizaje.

- **Determinación de salida:** Deciden si una neurona debe "activarse" o no, según la entrada ponderada.
- **Introducción de no linealidad:** Permiten que las redes neuronales aprendan relaciones complejas en los datos.
- **Facilitación del aprendizaje:** Son diferenciables, lo que permite el uso de algoritmos de optimización como el descenso del gradiente.

---

## 📚 Descripción General del Repositorio  
El repositorio `activation_functions_DemianMundo` incluye:
- Una carpeta `src`, donde se encuentran los scripts utilizados como módulos personalizados. Cada uno funciona como una librería para una función de activación.
- Un archivo `main.py`, que es el punto de entrada para ejecutar todas las gráficas de manera conjunta.
- Un archivo `requirements.txt` que contiene las dependencias necesarias para ejecutar el proyecto.
- Un archivo `.gitignore`, que especifica los archivos y carpetas que deben ser ignorados por Git.
- Un archivo `README.md`, que contiene la documentación del proyecto.

### Estructura del repositorio:
```
activation_functions_DemianMundo/
│── src/
│   │── step.py
│   │── sigmoid.py
│   │── gaussian.py
│   │── identity.py
│   │── piecewise.py
│   │── relu.py
│   │── sinusoidal.py
│   │── tanh.py
│
│── main.py
│── requirements.txt
│── .gitignore
│── README.md
```

---

## 🛠️ Desarrollo  
El proyecto incluye la implementación y visualización de las siguientes funciones de activación:

### 1️⃣ Función Escalón (Step)  
🎪 Activa la neurona solo cuando la entrada supera el umbral.  
🎪 Devuelve 0 si la entrada es menor que 0, y 1 si es mayor o igual a 0.  
🎪 Se utiliza en modelos simples de clasificación binaria.  

### 2️⃣ Función Sigmoide (Sigmoid)  
🎪 Transforma la entrada en un valor entre 0 y 1.  
🎪 Se usa en clasificación binaria y redes neuronales, aunque puede causar errores de gradiente desaparecido en redes profundas.

### 3️⃣ Función Gaussiana (Gaussian)  
🎪 Devuelve una curva en forma de campana centrada en 0.  
🎪 Se utiliza en redes neuronales radiales y modelos probabilísticos.

### 4️⃣ Función Identidad (Identity)  
🎪 Devuelve la misma entrada sin modificaciones.  
🎪 Se utiliza en regresión lineal y redes con salida continua.

### 5️⃣ Función Lineal a Trozos (Piecewise)  
🎪 Combina segmentos lineales para formar una función no lineal.  
🎪 Se usa en la aproximación de funciones complejas.

### 6️⃣ Función ReLU (Rectified Linear Unit)  
🎪 Devuelve 0 si la entrada es negativa y la entrada misma si es positiva.  
🎪 Es ampliamente usada en redes neuronales profundas debido a su eficiencia computacional.

### 7️⃣ Función Sinusoidal (Sinusoidal)  
🎪 Devuelve el valor del seno de la entrada.  
🎪 Se utiliza en modelos que procesan señales cíclicas o periódicas.

### 8️⃣ Función Tangente Hiperbólica (Tanh)  
🎪 Transforma la entrada en un valor entre -1 y 1.  
🎪 Se usa en clasificación y redes neuronales.  
🎪 Es similar a la sigmoide, pero centrada en 0, lo que mejora el aprendizaje en algunas redes.

---

## 📊 Conclusión  
La implementación de estas funciones de activación y su derivada permite visualizar su comportamiento y comprender su aplicación en proyectos de Machine Learning e Inteligencia Artificial.

---

## 📝 Notas Adicionales  
- El repositorio incluye un archivo `requirements.txt` para instalar los módulos necesarios.
- Se recomienda utilizar un entorno virtual para evitar conflictos entre dependencias.
- El código está organizado en módulos dentro de la carpeta `src` para facilitar su reutilización.

---

## 🛠️ Instrucciones de Configuración  
Pasos para configurar y utilizar este repositorio:

### 📌 Requisitos Previos  
- **Python** (versión 3.13 recomendada)  
- **Git**  

### 🔹 1️⃣ Clonar el Repositorio  
```bash
git clone https://github.com/DemianM21/activation_functions_DemianMundo.git
cd activation_functions_DemianMundo
```

### 🔹 2️⃣ Crear un Entorno Virtual  
```bash
python -m venv venv
```

### 🔹 3️⃣ Activar el Entorno Virtual  
- **Windows (PowerShell):**  
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (CMD):**  
  ```cmd
  venv\Scripts\activate.bat
  ```
- **Linux/Mac:**  
  ```bash
  source venv/bin/activate
  ```
Si PowerShell da error, ejecuta:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope Process
```

### 🔹 4️⃣ Instalar Dependencias  
```bash
pip install -r requirements.txt
```

### 🔹 5️⃣ Ejecutar el Proyecto  
```bash
python main.py
```

---

### 📌 Notas Adicionales  
Si necesitas desinstalar dependencias:
```bash
pip freeze > paquetes.txt
pip uninstall -r paquetes.txt -y
rm paquetes.txt  # (Linux/Mac)
del paquetes.txt  # (Windows)
```
Para actualizar `pip`:
```bash
python -m pip install --upgrade pip
```








