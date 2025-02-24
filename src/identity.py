'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt

'''
Se define la función identidad,
que toma el valor de "x" y lo devuelve sin modificar.
f(x) = x
'''
def identity(x):
    return x

'''
Cálculo de la derivada de la función f(x) = x.
Se obtiene f'(x) = 1.
'''
def identity_derivative(x):
    '''Crea un arreglo del mismo tamaño que x'''
    return np.ones_like(x) 

'''
Genera 400 puntos equidistantes en el rango de -10 a 10.
Los valores son utilizados para crear el eje x.
'''
x = np.linspace(-10, 10, 400)

'''La función identidad evalúa cada valor del arreglo x'''
y = identity(x)

'''La derivada de la función identidad evalúa cada valor del arreglo x'''
dy = identity_derivative(x)

'''
Configuración de la gráfica
'''
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Identidad') # Gráfica la función identidad con una linea continua
plt.plot(x, dy, label='Derivada de la Identidad', linestyle='dashed') #Gráfica la derivada de la función identidad con una linea discontinua
plt.axhline(0, color='black', linewidth=0.5) #define el color del eje "x" horizontal
plt.axvline(0, color='black', linewidth=0.5) #define el color del eje "y" vertical
plt.title("Función Identidad y su Derivada") #titulo de la gráfica
plt.legend()
plt.grid()
plt.show()
