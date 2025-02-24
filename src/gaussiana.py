'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt

'''
Se define la función gaussina
'''
def gaussian(x, A=1): # A representa la amplitud de la función.
    return A * np.exp(-x**2) #Calcula la exponencial de "-x^2".

'''
Se define la derivada de la función gaussiana
'''
def gaussian_derivative(x, A=1): 
    return -2 * x * gaussian(x, A) # Expresión matemática de la derivada de la función gaussiana.

'''
Genera 400 puntos equidistantes en el rango de -3 a 3.
Los valores son utilizados para crear el eje x.
'''
x = np.linspace(-3, 3, 400) # Genera un arreglo de 400 puntos en el rango de -3 a 3, la valores son utilizados para el eje "x".
y = gaussian(x) # Evalua la función en cada punto del arreglo.
dy = gaussian_derivative(x) # Evalua la función en cada punto del arreglo.

plt.figure(figsize=(8, 5)) # Se define el tamaño de la figura.
plt.plot(x, y, label='Gaussiana') #Se gráfica la función con una linea continua.
plt.plot(x, dy, label='Derivada de la Gaussiana', linestyle='dashed') #Se gráfica la derivada de la función con una linea discontinua.
plt.axhline(0, color='black', linewidth=0.5) # Define color y ancho del eje "x".
plt.axvline(0, color='black', linewidth=0.5) # Define color y ancho del eje "y".
plt.title("Función Gaussiana y su Derivada") # Define el titulo de la gráfica.
plt.legend() # Etiqueta las funciones.
plt.grid()  # Agrega una cuadrícula a la gráfica.
plt.show() #Muestra la figura en una ventana.