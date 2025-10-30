'''
import matplotlib.pyplot as plt
import numpy as np
import math

# Datos
x = np.linspace(0, 10, 100)
y = np.sin(x)


x = []
y = []
for i in range(100):
    dato = i/100
    x.append(dato)

for j in range(len(x)):
    dato = math.cos(2*math.pi*x[j])
    y.append(dato)
# x = [1,3,4,5,6,8]
# y = [3,5,7,4,3,1]
# Crear la gráfica
plt.scatter(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Seno')
plt.xlabel('X')
plt.ylabel('sin(X)')

# Mostrar la gráfica
plt.show()
'''
import matplotlib.pyplot as plt

# Datos
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 12]

# Crear la gráfica de barras
plt.bar(categorias, valores, color=['red', 'blue', 'green', 'orange'])

# Agregar título y etiquetas
plt.title('Gráfica de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar la gráfica
plt.show()
