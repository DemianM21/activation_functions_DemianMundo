import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(x, A=1, omega=1, phi=0):
    return A * np.sin(omega * x + phi)

def sinusoidal_derivative(x, A=1, omega=1, phi=0):
    return A * omega * np.cos(omega * x + phi)

x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = sinusoidal(x)
dy = sinusoidal_derivative(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sinusoidal')
plt.plot(x, dy, label='Derivada de la Sinusoidal', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Función Sinusoidal y su Derivada")
plt.legend()
plt.grid()
plt.show()
