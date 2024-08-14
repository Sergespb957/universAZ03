# Построение диаграммы рассеяния для двух наборов случайных данных


import numpy as np
import matplotlib.pyplot as plt
# Генерация двух наборов случайных данных
x = np.random.rand(100)  # массив из 100 случайных чисел по оси X
y = np.random.rand(100)  # массив из 100 случайных чисел по оси Y

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, color='red')
plt.title('Диаграмма рассеяния')
plt.xlabel('Случайные данные X')
plt.ylabel('Случайные данные Y')
plt.grid()
plt.show()
