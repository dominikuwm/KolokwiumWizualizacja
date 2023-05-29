import matplotlib.pyplot as plt
import numpy as np

# Tworzenie danych dla funkcji y = x^2
x = np.linspace(0, 4, 100)
y1 = x**2

# Tworzenie danych dla funkcji y = e^x
y2 = np.exp(x)

# Tworzenie danych dla funkcji y = x^x
y3 = x**x

# Tworzenie subplotów
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

# Wykres dla funkcji y = x^2
ax1.plot(x, y1, color='red', linestyle='dashed')
ax1.set_title('y = x^2')

# Wykres dla funkcji y = e^x
ax2.plot(x, y2, color='green', linestyle='dashdot')
ax2.set_title('y = e^x')

# Wykres dla funkcji y = x^x
ax3.plot(x, y3, color='blue', linestyle='dotted')
ax3.set_title('y = x^x')

# Dodanie legendy na górze dla wszystkich subplotów
plt.legend(['y = x^2', 'y = e^x', 'y = x^x'], loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)

# Wyświetlenie subplotów
plt.tight_layout()
plt.show()
