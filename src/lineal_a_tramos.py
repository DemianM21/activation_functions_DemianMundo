import numpy as np
import matplotlib.pyplot as plt

def piecewise(x):
    return np.piecewise(x, [x < -1, (-1 <= x) & (x <= 1), x > 1], [-1, lambda x: x, 1])

def piecewise_derivative(x):
    return np.piecewise(x, [x < -1, (-1 <= x) & (x <= 1), x > 1], [0, 1, 0])

x = np.linspace(-3, 3, 400)
y = piecewise(x)
dy = piecewise_derivative(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Lineal a Tramos')
plt.plot(x, dy, label='Derivada de la Lineal a Tramos', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Función Lineal a Tramos y su Derivada")
plt.legend()
plt.grid()
plt.show()
