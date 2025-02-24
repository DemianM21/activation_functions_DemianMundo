'''
Paquetes o módulos utilizados
'''
import numpy as np
import matplotlib.pyplot as plt
'''
Se define la función sinusoidal
'''
def sinusoidal(x, A=1, omega=1, phi=0):
    '''
    A = amplitud, omega = frecuencia angular, phi = desfase 
    '''
    return A * np.sin(omega * x + phi) # Escala la función seno por la amplitud.
'''
Se define la derivada de la función sinusoidal
'''

def sinusoidal_derivative(x, A=1, omega=1, phi=0):
    '''
    A = amplitud, omega = frecuencia angular, phi = desfase 
    '''
    return A * omega * np.cos(omega * x + phi) # Calcula el coseno del angulo.

'''
Genera 400 puntos equidistantes en el rango de -2pi a 2pi.
Los valores son utilizados para crear el eje x.
'''
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = sinusoidal(x) # Evalúa la función en cada valor del arreglo.
dy = sinusoidal_derivative(x) # Evalúa la derivada de la función en cada valor del arreglo.

'''
Configuración de la gráfica
'''
plt.figure(figsize=(8, 5)) # Tamaño de la figura.
plt.plot(x, y, label='Sinusoidal') # Se gráfica la función con una linea continua.
plt.plot(x, dy, label='Derivada de la Sinusoidal', linestyle='dashed') # Se gráfica la derivada de la función con una linea discontinua.
plt.axhline(0, color='black', linewidth=0.5) # Ancho y color del eje "x".
plt.axvline(0, color='black', linewidth=0.5) # Ancho y color del eje "y".
plt.title("Función Sinusoidal y su Derivada") # Titulo de la figura.
plt.legend() # Se definen las etiquetas de la función y su derivada.
plt.grid() # Se crea una cuadricula en la gráfica.
plt.show() # Se muestra la figura en una ventana.
