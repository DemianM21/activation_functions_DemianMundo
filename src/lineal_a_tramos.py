'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt

'''
Se define la función lineal a tramos
'''
def piecewise(x): #Se define la función lineal a tramos.
    '''
    Si x < -1: la función de vuelve -1
    Si (-1 <= x) & (x <=1): la función devuelve una "x" (una línea recta con pendiente 1)
    Si x > 1: la función devuelve 1
    '''
    return np.piecewise(x, [x < -1, (-1 <= x) & (x <= 1), x > 1], [-1, lambda x: x, 1])  #función de numpy que permite definir funciones por partes.

'''
Se define la derivada de la función lineal a tramos
'''
def piecewise_derivative(x): #se define la derivada de la función lineal a tramos.
    '''
    Si x < -1: la función de vuelve 0
    Si (-1 <= x) & (x <=1): la derivada es 1.
    Si x > 1: la función devuelve 0
    '''
    return np.piecewise(x, [x < -1, (-1 <= x) & (x <= 1), x > 1], [0, 1, 0])

'''
Genera 400 puntos equidistantes en el rango de -3 a 3.
Los valores son utilizados para crear el eje x.
'''
x = np.linspace(-3, 3, 400) 
y = piecewise(x) #Evalua los valores del arreglo en la función.
dy = piecewise_derivative(x) #Evalua los valores del arreglo en la derivada de la función.

'''
Configuración de la gráfica
'''
plt.figure(figsize=(8, 5)) #Se establece el tamaño de la gráfica.
plt.plot(x, y, label='Lineal a Tramos') #Se gráfica la función con linea continua.
plt.plot(x, dy, label='Derivada de la Lineal a Tramos', linestyle='dashed') # Gráfica la derivada de la función con una linea discontinua.
plt.axhline(0, color='black', linewidth=0.5) # Define el tamaño y color del eje "x".
plt.axvline(0, color='black', linewidth=0.5) # Define el tamaño y color del eje "y".
plt.title("Función Lineal a Tramos y su Derivada") # Establece el titulo de la gráfica.
plt.legend() # Etiqueta las función y la derivada.
plt.grid() # Crea una cuadricula sobre la gráfica.
plt.show() # Muestra la figura en una ventana.
