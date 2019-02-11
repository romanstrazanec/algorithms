import numpy as np
import matplotlib.pyplot as plt


def circle(x, inverse=False):
  m = np.max(x)
  c = (m + np.min(x)) / 2
  r = m - c
  s = np.sqrt(r*r-(x-c)*(x-c))
  return -s if inverse else s


def recaman(n_iterations=10, n_middle_vals=10, **kwargs):
  step = 1
  pos = 0
  occupied = set()
  while step <= n_iterations:
    occupied.add(pos)
    next_pos = pos - step
    if next_pos < 0 or next_pos in occupied:
      next_pos = pos + step
    x = np.linspace(pos, next_pos, abs(next_pos-pos)*n_middle_vals)
    plt.plot(x, circle(x, step % 2), **kwargs)
    pos = next_pos
    step += 1
  plt.axis('off')
  plt.savefig(f"recaman{n_iterations}.png", dpi=600, papertype='a4')


recaman(40, 20)