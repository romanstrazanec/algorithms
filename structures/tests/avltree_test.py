from random import randint
from structures.avltree import AVLTree as A
from structures.plot_tree import plot_tree as pt

a = A()


def p(k): a.put(k, f"{k}-value")


keys = set(randint(0, 100) for _ in range(10))

for k in keys:
    p(k)

print(a)
pt(a, text=lambda node: f"{node.balance_factor}")
