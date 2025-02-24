'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt

'''
Importación de funciones desde módulos personalizados
'''
from src.sigmoidal import sigmoid
from src.escalon import step
from src.gaussiana import gaussian
from src.identity import identity
from src.lineal_a_tramos import piecewise
from src.relu import relu
from src.sinusoidal import sinusoidal
from src.tangente_hiperbolica import tanh

def main():
    # Definimos un rango de valores
    x = np.linspace(-10, 10, 400)
    
    # Calculamos la salida de cada función
    y_sigmoid     = sigmoid(x)
    y_step        = step(x)
    y_gaussian    = gaussian(x)
    y_identity    = identity(x)
    y_piecewise   = piecewise(x)
    y_relu        = relu(x)
    y_sinusoidal  = sinusoidal(x)
    y_tanh        = tanh(x)
    
    # Configuramos los subplots para graficar cada función
    fig, axs = plt.subplots(4, 2, figsize=(12, 12))
    axs = axs.flatten()
    
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
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
