import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

x = np.linspace(-10, 10, 400)
y = sigmoid(x)
dy = sigmoid_derivative(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sigmoide')
plt.plot(x, dy, label='Derivada de la Sigmoide', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Función Sigmoide y su Derivada")
plt.legend()
plt.grid()
plt.show()