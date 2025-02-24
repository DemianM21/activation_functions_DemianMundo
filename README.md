FUNCIONES DE ACTIVACIÓN
Fecha: 10 de octubre de 2023  
Autor: Demian Mundo

Introducción:  
Este proyecto tiene como objetivo mostrar cómo gráficar 8 tipos de funciones de
activación comunes en el ámbito de maching learning y inteligencia artificial. Además,
se proporciona una guía para configurar y utilizar este repositorio en tu computadora.

Objetivo:  
Conocer las funciones de activación.
Gráficar y visualizar las funciones de activación realizadas en python.
Facilitar la reutiliación del codigo mediante un repositorio organizado.

Desarrollo:  
El proyecto incluye la implementación de las siguientes funciones de activación:

- Función Escalón (Step): 

Devuelve 0 si la entrada es menor que 0, y 1 si es mayor o igual a 0.
Se utiliza para la clasificación binaria.

-Función Sigmoide (Sigmoid):

Transforma la entrada en un valor entre 0 y 1.
Se utiliza para clasificación binaria y redes neuronales.

-Función Gaussiana (Gaussian)

Devuelve una curva en forma de campana centrada en 0.
Se utiliza en redes neuronales radiales.

-Función Identidad (Identity):

Devuelve la misma entrada sin modificaciones
Se utiliza en regresión lineal

-Función lineal a trozos (Piecewise):

Combina segmentos lineales para formar una función no lineal.
Se utiliza en aproximación de funciones complejas.

-Función Relu (Rectified Linear Unit):

Devuelve 0 si la entrada en negativa. y la entrada misma si es positiva.
Se usa en redes neuronales profundas.

-Función Sinusoidal (Sinusoidal):

Devuelve el valor del seno de la entrada.
Se utiliza en modelos periódicos.

-Función Tangente Hiperbólica (Tanh):

Transforma la entrada en un valor entre -1 y 1.
Se usa en la clasificación y redes neuronales


Conclusión:  
La implementación de estas funciones de activación permite visualizar su comportamiento, para aplicarlas en 
proyectos de maching learning.

Notas adicionales:  

-El repositorio incluye un archivo "requirements.txt" para instalar los modulos necesarios
-Se recomienda utilizar un entorno virtual, para evitar conflictos.
-El código esta organizado en módulos dentro de la carpeta "src" para facilitar su reutilización.


Instrucciones para usar el repositorio:

1. Clona el repositorio en tu computadora.
2. Crea un entorno virtual (env) e instala las dependencias:

python -m venv env
source env/bin/activate  # En Linux/Mac

env\Scripts\activate     # En Windows
pip install -r requirements.txt

3. Ejecuta el archivo "main.py" para visualizar las gráficas de las funciones de activación.
