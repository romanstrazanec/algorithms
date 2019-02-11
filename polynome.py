import numpy as np
import matplotlib.pyplot as plt

def show_lines(x, y):
    for i in y:
        lw = .6 if i == 0 else .3
        plt.plot(x, [i for _ in x], lw=lw, color='k')

    for i in range(int(min(x)), int(max(x)) + 1):
        lw = .6 if i == 0 else .3
        plt.plot([i for _ in y], y, lw=lw, color='k')

def polynome(**kwargs):
    try:
        x = kwargs['x']
        factors = kwargs['factors']
    except Exception:
        return np.nan
    if type(factors) == list or type(factors) == tuple:
        l = len(factors)
        return sum((factors[i] * x ** (l - i - 1) for i in range(l)))
    if type(factors) == dict:
        return sum((factors[i] * x ** int(i) for i in factors))

x = np.linspace(-2, 2, 101)
plt.plot(x, polynome(x=x, factors={3: 1}))
# plt.plot(x, polynome(x=x, factors=[1, 0, 0]))
plt.show()