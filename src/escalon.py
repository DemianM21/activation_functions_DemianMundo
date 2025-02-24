'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt

'''
Se define la función escalon
'''
def step(x):
    return np.where(x >= 0, 1, 0) #Devuelve 1 si x>=0 y devuelve 0 si x<0 (función de numpy).

'''
Se define la derivada de la función escalon
'''
def step_derivative(x):
    return np.zeros_like(x) #Crea un arreglo del mismo tamaño que "x", donde todos los elementos son 0.

'''
Genera 400 puntos equidistantes en el rango de -10 a 10.
Los valores son utilizados para crear el eje x.
'''
x = np.linspace(-10, 10, 400)
y = step(x) #La función escalón evalúa cada valor del arreglo x.
dy = step_derivative(x) #La derivada de la función escalón evalúa cada valor del arreglo x.

'''
Configuracón de la gráfica
'''
plt.figure(figsize=(8, 5)) # Tamaño de la figura.
plt.plot(x, y, label='Escalón') # Gráfica la función escalón con una linea continua.
plt.plot(x, dy, label='Derivada del Escalón', linestyle='dashed') # Gráfica la derivada de la función con una linea discontinua.
plt.axhline(0, color='black', linewidth=0.5) # Establece el color del eje de las abcisas.
plt.axvline(0, color='black', linewidth=0.5) #Establece el color del eje de las ordenadas.
plt.title("Función Escalón y su Derivada") #Se define el titulo de la gráfica.
plt.legend() # Muestra las etiquetas correspondientes a cada gráfica.
plt.grid() # Crea una cuadricula en la gráfica.
plt.show() #Muestra la gráfica en una ventana.