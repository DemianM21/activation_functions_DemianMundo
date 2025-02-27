'''
Paquetes o módulos utilizados
'''
import numpy as np                           # Biblioteca para operaciones matemáticas y manejo de arrays
import matplotlib.pyplot as plt              # Biblioteca para generar gráficos

'''
Importación de funciones desde módulos personalizados
Estas funciones definen diferentes transformaciones o activaciones que queremos graficar
'''
from src.sigmoidal import sigmoid             # Función sigmoidal
from src.escalon import step                  # Función escalón
from src.gaussiana import gaussian            # Función gaussiana
from src.identity import identity             # Función identidad
from src.lineal_a_tramos import piecewise       # Función lineal a tramos
from src.relu import relu                     # Función ReLU (Rectified Linear Unit)
from src.sinusoidal import sinusoidal         # Función sinusoidal
from src.tangente_hiperbolica import tanh       # Función tangente hiperbólica  

def main():
    # Definimos un rango de valores para el eje x: desde -10 hasta 10 con 400 puntos equidistantes
    x = np.linspace(-10, 10, 400)
    
    # Calculamos la salida de cada función aplicándola al vector x
    y_sigmoid     = sigmoid(x)
    y_step        = step(x)
    y_gaussian    = gaussian(x)
    y_identity    = identity(x)
    y_piecewise   = piecewise(x)
    y_relu        = relu(x)
    y_sinusoidal  = sinusoidal(x)
    y_tanh        = tanh(x)
    
    # Configuramos la figura y los subplots: 4 filas x 2 columnas para poder graficar las 8 funciones
    fig, axs = plt.subplots(4, 2, figsize=(12, 12))
    axs = axs.flatten()  # Convertimos la matriz de ejes en un arreglo unidimensional para facilitar la asignación
    
    # Graficamos cada función en su respectivo subplot y asignamos un título que indique de qué función se trata
    axs[0].plot(x, y_sigmoid)
    axs[0].set_title("Función Sigmoidal")
    
    axs[1].plot(x, y_step)
    axs[1].set_title("Función Escalón")
    
    axs[2].plot(x, y_gaussian)
    axs[2].set_title("Función Gaussiana")
    
    axs[3].plot(x, y_identity)
    axs[3].set_title("Función Identidad")
    
    axs[4].plot(x, y_piecewise)
    axs[4].set_title("Función Lineal a tramos")
    
    axs[5].plot(x, y_relu)
    axs[5].set_title("Función ReLU")
    
    axs[6].plot(x, y_sinusoidal)
    axs[6].set_title("Función Sinusoidal")
    
    axs[7].plot(x, y_tanh)
    axs[7].set_title("Función Tangente Hiperbólica")
    
    # Ajustamos el layout de la figura para evitar la superposición de etiquetas y gráficos
    plt.tight_layout()
    # Mostramos la figura con todos los subplots
    plt.show()

# Este bloque asegura que main() se ejecute solo cuando el script se corre directamente,
# y no cuando se importa como módulo en otro script
if __name__ == "__main__":
    main()
    
    
    
    
    
    
