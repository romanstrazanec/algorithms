import numpy as np
import matplotlib.pyplot as plt

def show_lines(x, y):
    for i in y:
        lw = .6 if i == 0 else .3
        plt.plot(x, [i for _ in x], lw=lw, color='k')

    for i in range(int(min(x)), int(max(x)) + 1):
        lw = .6 if i == 0 else .3
        plt.plot([i for _ in y], y, lw=lw, color='k')

def xlinspace(x):
    return np.linspace(-x * np.pi, x * np.pi, 101)

def yrange(*args):
    ymin = int(min([min(i) for i in args])) - 1
    ymax = int(max([max(i) for i in args])) + 1
    return range(ymin, ymax)

def polynome(**kwargs):
    try:
        x = kwargs['x']
        factors = kwargs['factors']
    except Exception:
        return np.nan
    if type(factors) == list:
        l = len(factors)
        return sum((factors[i] * x ** (l - i - 1) for i in range(l)))
    if type(factors) == dict:
        return sum((factors[i] * x ** i for i in factors))

def cos_polynome(x, max_polynome):
    return polynome(x=x, factors={i: ((i + 2) % 4 - 1) * 1 / np.prod(range(2, i + 1)) for i in range(0, max_polynome + 1, 2)})

def cos_polynomes(start=2, stop=2):
    return {max_polynome: np.array([cos_polynome(i, max_polynome) for i in x]) for max_polynome in range(start, stop + 1, 2)}


x = xlinspace(1.2)
ycos = np.array([np.cos(i) for i in x])
y = cos_polynomes(2, 4)

plt.plot(x, ycos, label='cos(x)')
for i in y:
    plt.plot(x, y[i], label=f"x^{i}")

show_lines(x, yrange(ycos, *[y[i] for i in y]))
plt.legend()
plt.show()