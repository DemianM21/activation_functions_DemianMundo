'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt
'''
Se define la función sigmoide
'''
def sigmoid(x):
    '''
    Mapea cualquier valor real "x" aun valor en el rango (0,1)
    '''
    return 1 / (1 + np.exp(-x))
'''
Se define la derivada de la función sigmoide
'''
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x)) # Deriva la propiedad de la función sigmoide.

'''
Genera 400 puntos equidistantes en el rango de -10 a 10.
Los valores son utilizados para crear el eje x.
'''
x = np.linspace(-10, 10, 400)
y = sigmoid(x) # Evalúa la función en cada valor del arreglo.
dy = sigmoid_derivative(x) # Evalúa la derivada de la función en cada valor del arreglo.

'''
Configuración de la gráfica
'''
plt.figure(figsize=(8, 5)) # Tamaño de la figura.
plt.plot(x, y, label='Sigmoide') # Se gráfica la función con una linea continua.
plt.plot(x, dy, label='Derivada de la Sigmoide', linestyle='dashed') # Se gráfica la derivada de la función con una linea discontinua.
plt.axhline(0, color='black', linewidth=0.5) # Ancho y color del eje "x".
plt.axvline(0, color='black', linewidth=0.5) # Ancho y color del eje "y".
plt.title("Función Sigmoide y su Derivada") # Titulo de la figura.
plt.legend() # Se definen las etiquetas de la función y su derivada.
plt.grid() # Se crea una cuadricula en la gráfica.
plt.show() # Se muestra la figura en una ventana.