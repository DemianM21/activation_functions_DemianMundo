import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

x = np.linspace(-3, 3, 400)
y = relu(x)
dy = relu_derivative(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='ReLU')
plt.plot(x, dy, label='Derivada de ReLU', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Función ReLU y su Derivada")
plt.legend()
plt.grid()
plt.show()
