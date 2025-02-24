import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, A=1):
    return A * np.exp(-x**2)

def gaussian_derivative(x, A=1):
    return -2 * x * gaussian(x, A)

x = np.linspace(-3, 3, 400)
y = gaussian(x)
dy = gaussian_derivative(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Gaussiana')
plt.plot(x, dy, label='Derivada de la Gaussiana', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Función Gaussiana y su Derivada")
plt.legend()
plt.grid()
plt.show()