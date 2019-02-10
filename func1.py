import numpy as np
import matplotlib.pyplot as plt

def max_func(x, n):
    try:
        return 1 / n * np.sin(n * np.pi * x) + max_func(x, n + 2)
    except RecursionError:
        return 0

def func(x, n, step=2):
    return 4/np.pi * sum((1/i * np.sin(i * np.pi * x) for i in range(1, n, step)))


r = 1
x = np.linspace(-r, r,101)

# plt.plot(x, [max_func(i, 1) for i in x], label="max")
for j in range(3,10,2):
    plt.plot(x, [func(i, j) for i in x], label=j)

plt.legend()
plt.show()