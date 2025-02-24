import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x)**2

x = np.linspace(-3, 3, 400)
y = tanh(x)
dy = tanh_derivative(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Tangente Hiperbólica')
plt.plot(x, dy, label='Derivada de la Tangente Hiperbólica', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Función Tangente Hiperbólica y su Derivada")
plt.legend()
plt.grid()
plt.show()