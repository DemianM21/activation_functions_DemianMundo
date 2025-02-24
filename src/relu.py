'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt

'''
Se define la función Relu
'''
def relu(x):
    '''
    Devuelve el máximo entre 0 y x.
    Si x>=0, la función devuleve x.
    Si x< 0, la función devuelve 0.
    '''
    return np.maximum(0, x) 

'''
Se define la derivada de la función Relu
'''
def relu_derivative(x): 
    '''
    Devuelve:
    1, Si x>0
    0, Si x<=0
    '''
    return np.where(x > 0, 1, 0) 

'''
Genera 400 puntos equidistantes en el rango de -3 a 3.
Los valores son utilizados para crear el eje x.
'''
x = np.linspace(-3, 3, 400)
y = relu(x) #Evalúa la función relu en cada valor del arreglo.
dy = relu_derivative(x) #Evalúa la derivada de la función relu en cada valor del arreglo.

'''
Configuración de la gráfica
'''
plt.figure(figsize=(8, 5)) #Establece el tamaño de la figura.
plt.plot(x, y, label='ReLU') # La función se gráfica con una linea continua.
plt.plot(x, dy, label='Derivada de ReLU', linestyle='dashed') #La derivada de la función se gráfica con una linea discontinua.
plt.axhline(0, color='black', linewidth=0.5) # Ancho y color del eje "x".
plt.axvline(0, color='black', linewidth=0.5) # Ancho y color del eje "y".
plt.title("Función ReLU y su Derivada") # Se define el titulo de la gráfica.
plt.legend() # Se etiqueta la función y la derivada.
plt.grid() # Se agrega cuadrícula a la gráfica.
plt.show() # Muestra la figura en una ventana.
