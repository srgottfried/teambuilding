import matplotlib.pyplot as plt
import numpy as np


def read(filename: str):
    with open(filename, "r") as f:
        a_vals, b_vals = [], []
        for linea in f:
            a, b = linea.strip().split(",")
            a_vals.append(float(a))
            b_vals.append(float(b))
    return a_vals, b_vals


def plot(filename: str, color: str, label: str):
    a, b = read(filename)
    x = np.array(a)
    y = np.array(b)
    plt.scatter(x, y, c=color, label=label)
    if len(x) != 0:
        m, b = np.polyfit(x, y, 1)
        model = np.poly1d([m, b])
        x_regresion = np.linspace(min(x), max(x), 100)
        y_regresion = model(x_regresion)
        plt.plot(x_regresion, y_regresion, c=color)


plt.figure(figsize=(10, 6))
plot("logs/go.log", "red", "Goroutine")
plot("logs/multiprocessing.log", "green", "Python multiprocessing")
plot("logs/multithreading.log", "blue", "Python multithreading")
plt.plot()
plt.title("")
plt.xlabel("Tasks")
plt.ylabel("Seconds")
plt.legend()
plt.show()
