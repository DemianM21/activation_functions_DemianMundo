'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt
'''
Se define la función tanh
'''
def tanh(x):
    return np.tanh(x) #Esta función mapea cualquier valor real x a un valor en el rango -1 a 1.
'''
Se define la derivada de la función tanh
'''
def tanh_derivative(x):
    return 1 - np.tanh(x)**2 # Expresión matemática de la derivada de la función tangente hiperbólica. 

'''
Genera 400 puntos equidistantes en el rango de -3 a 3.
Los valores son utilizados para crear el eje x.
'''
x = np.linspace(-3, 3, 400)
y = tanh(x) # Evaluá la función en cada valor del arreglo.
dy = tanh_derivative(x) # Evaluá la derivada en cada valor del arreglo.

'''
Configuración de la gráfica
'''
plt.figure(figsize=(8, 5)) # Tamaño de la figura.
plt.plot(x, y, label='Tangente Hiperbólica') # Se gráfica la función con una linea continua.
plt.plot(x, dy, label='Derivada de la Tangente Hiperbólica', linestyle='dashed') # Se gráfica la derivada de la función con una linea discontinua.
plt.axhline(0, color='black', linewidth=0.5) # Ancho y color del eje "x".
plt.axvline(0, color='black', linewidth=0.5) # Ancho y color del eje "y".
plt.title("Función Tangente Hiperbólica y su Derivada") # Titulo de la figura.
plt.legend() # Se definen las etiquetas de la función y su derivada.
plt.grid() # Se crea una cuadricula en la gráfica.
plt.show() # Se muestra la figura en una ventana.