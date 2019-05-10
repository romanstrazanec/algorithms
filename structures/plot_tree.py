import matplotlib.pyplot as plt


def plot_tree(tree, c='k'):
    if tree.root:
        plt.scatter(0, 0, c=c)
        if tree.root.has_left_child():
            plt.plot([0, -1], [0, -1], c=c)
            _plt_left(tree.root.left_child, c=c)
        if tree.root.has_right_child():
            plt.plot([0, 1], [0, -1], c=c)
            _plt_right(tree.root.right_child, c=c)
        plt.show()


def _plt_left(node, x=-1., y=-1., l=2, c='k'):
    # TODO: correct the position computing
    plt.scatter(x, y, c=c)
    if node.has_left_child():
        nx, ny = x / l - 2, y - 1
        plt.plot([x, nx], [y, ny], c=c)
        _plt_left(node.left_child, nx, ny, l * 2, c)
    if node.has_right_child():
        nx, ny = x / l - 1, y - 1
        plt.plot([x, nx], [y, ny], c=c)
        _plt_left(node.right_child, nx, ny, l * 2, c)


def _plt_right(node, x=1., y=-1., l=2, c='k'):
    plt.scatter(x, y, c=c)
    if node.has_right_child():
        nx, ny = x / l + 2, y - 1
        plt.plot([x, nx], [y, ny], c=c)
        _plt_right(node.right_child, nx, ny, l * 2, c)
    if node.has_left_child():
        nx, ny = x / l + 1, y - 1
        plt.plot([x, nx], [y, ny], c=c)
        _plt_right(node.left_child, nx, ny, l * 2, c)
