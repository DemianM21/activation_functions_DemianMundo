import numpy as np
import matplotlib.pyplot as plt

def step(x):
    return np.where(x >= 0, 1, 0)

def step_derivative(x):
    return np.zeros_like(x)

x = np.linspace(-10, 10, 400)
y = step(x)
dy = step_derivative(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Escalón')
plt.plot(x, dy, label='Derivada del Escalón', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Función Escalón y su Derivada")
plt.legend()
plt.grid()
plt.show()