import numpy as np
import time
from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

time_start_1 = time.perf_counter()
# Задание №1
# Выполнение программы для стандартных списков

arr1 = []
arr2 = []
arr = []
for i in range(10**6):
    arr1.append(randint(-10, 10))
    arr2.append(randint(-10, 10))


for i in range (10**1):
    arr.append(arr1[i] * arr2[i])
print('Время без использования библиотеки = ', time.perf_counter() - time_start_1)

# Выполнение программы для массиву numpy
time_start_2 = time.perf_counter()

arr1_1 = np.random.randint(-10, 10, 10**6)
arr2_1 = np.random.randint(-10, 10, 10**6)
arr_1 = np.multiply(arr1_1, arr2_1)

print('Время с использованием библиотеки = ', time.perf_counter() - time_start_2)

# Задание №2
arr_data = np.genfromtxt('data2.csv', delimiter=',')
arr_data = arr_data[1:]

solids = arr_data[:, 2]

# Построение гистрограммы для 3 столбца
def Solid():

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.hist(solids, 40, color = 'Lightgreen', ec = 'Green')
    plt.title('Гистрограмма')
    plt.xlabel('Примеси')
    plt.ylabel('Частота')
    plt.show()

if __name__ == "__main__":
    Solid()

# Построение нормализованной гистрограммы для 3 столбца
def Solid():

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.hist(solids, 40, color = 'Lightgreen', ec = 'Green', density = True)
    plt.title('Нормализованная гистрограмма')
    plt.xlabel('Примеси')
    plt.ylabel('Частота')
    plt.show()

Solid()
# Вычисление среднеквадратичного отклонения


print('Среднеквадратичное отклонение = ', np.std(solids))

# Задание 3

def plot3d():
    xs = np.linspace(-np.pi, np.pi, 20)
    ys = 1/xs
    zs = np.sin(xs)

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(projection = '3d')
    ax.plot(xs, ys, zs, marker='x', color='red')
    plt.title('Объемный график')
    plt.show()

plot3d()

# Дополнительное задание



fig = plt.figure(figsize = (6,4))
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2, color='Red')

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(-2, 2, 1000)
    y = np.sin(0.25*np.pi*(x - 0.04 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
plt.show()

