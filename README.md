# 🧠 Funciones de Activación en Machine Learning

## 📅 Fecha: 10 de octubre de 2023  
## 👤 Autor: Demian Mundo  

---

## 🚀 Introducción  
Este proyecto tiene como objetivo mostrar cómo graficar 8 tipos de funciones de activación comunes en el ámbito de machine learning e inteligencia artificial. Además, se proporciona una guía paso a paso para configurar y utilizar este repositorio en tu computadora.

---

## 🎯 Objetivo  
- Conocer y entender las funciones de activación más utilizadas en machine learning.  
- Graficar y visualizar estas funciones utilizando Python.  
- Facilitar la reutilización del código mediante un repositorio organizado y modular.  

---

## 🛠️ Desarrollo  
El proyecto incluye la implementación y visualización de las siguientes funciones de activación:

### 1️⃣ Función Escalón (Step)  
🔹 Devuelve 0 si la entrada es menor que 0, y 1 si es mayor o igual a 0.  
🔹 Se utiliza para la clasificación binaria.  

### 2️⃣ Función Sigmoide (Sigmoid)  
🔹 Transforma la entrada en un valor entre 0 y 1.  
🔹 Se utiliza en clasificación binaria y redes neuronales.  

### 3️⃣ Función Gaussiana (Gaussian)  
🔹 Devuelve una curva en forma de campana centrada en 0.  
🔹 Se utiliza en redes neuronales radiales.  

### 4️⃣ Función Identidad (Identity)  
🔹 Devuelve la misma entrada sin modificaciones.  
🔹 Se utiliza en regresión lineal.  

### 5️⃣ Función Lineal a Trozos (Piecewise)  
🔹 Combina segmentos lineales para formar una función no lineal.  
🔹 Se utiliza en la aproximación de funciones complejas.  

### 6️⃣ Función ReLU (Rectified Linear Unit)  
🔹 Devuelve 0 si la entrada es negativa y la entrada misma si es positiva.  
🔹 Es ampliamente usada en redes neuronales profundas.  

### 7️⃣ Función Sinusoidal (Sinusoidal)  
🔹 Devuelve el valor del seno de la entrada.  
🔹 Se utiliza en modelos periódicos.  

### 8️⃣ Función Tangente Hiperbólica (Tanh)  
🔹 Transforma la entrada en un valor entre -1 y 1.  
🔹 Se usa en clasificación y redes neuronales.  

---

## 📊 Conclusión  
La implementación de estas funciones de activación permite visualizar su comportamiento y comprender su aplicación en proyectos de machine learning e inteligencia artificial.

---

## 📝 Notas Adicionales  
- El repositorio incluye un archivo `requirements.txt` para instalar los módulos necesarios.  
- Se recomienda utilizar un entorno virtual para evitar conflictos entre dependencias.  
- El código está organizado en módulos dentro de la carpeta `src` para facilitar su reutilización.  

---

## 🛠️ Instrucciones de Configuración  
Sigue estos pasos para configurar y ejecutar el proyecto correctamente.

### 📌 Requisitos Previos  
Antes de comenzar, asegúrate de tener instalado:
- **Python** (versión 3.x recomendada)
- **Git**

### 🔹 1️⃣ Clonar el Repositorio  
Abre la terminal (CMD, PowerShell o Git Bash) en la carpeta donde deseas guardar el proyecto y ejecuta:

```bash
git clone https://github.com/DemianM21/activation_functions_DemianMundo.git
```
Luego, entra en la carpeta del proyecto:

```bash
cd activation_functions_DemianMundo
```

### 🔹 2️⃣ Crear un Entorno Virtual  
Ejecuta el siguiente comando para crear un entorno virtual:

```bash
python -m venv venv
```

### 🔹 3️⃣ Activar el Entorno Virtual  

#### En PowerShell (Windows):  
```powershell
.\venv\Scripts\Activate.ps1
```

#### En CMD (Windows):  
```cmd
venv\Scripts\activate.bat
```

#### En Git Bash o WSL (Linux/Mac):  
```bash
source venv/bin/activate
```

Si la activación en PowerShell da error, ejecuta:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope Process
```
y vuelve a intentarlo.

### 🔹 4️⃣ Instalar Dependencias  
Ejecuta el siguiente comando para instalar los paquetes necesarios:

```bash
pip install -r requirements.txt
```

### 🔹 5️⃣ Ejecutar el Proyecto  
Para correr el archivo principal del proyecto, usa:

```bash
python main.py
```

---

### 📌 Notas Adicionales  
Si necesitas desinstalar todas las dependencias, usa:

```bash
pip freeze > paquetes.txt
pip uninstall -r paquetes.txt -y
del paquetes.txt  # (Windows)
rm paquetes.txt   # (Linux/Mac)
```

Si tienes problemas con `pip`, asegúrate de actualizarlo:

```bash
python -m pip install --upgrade pip
```

