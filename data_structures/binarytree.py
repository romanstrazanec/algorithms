class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def pre_order(self, func, *args, **kwargs):
        func(self.key, *args, **kwargs)
        if self.left_child:
            self.left_child.pre_order(func, *args, **kwargs)
        if self.right_child:
            self.right_child.pre_order(func, *args, **kwargs)

    def post_order(self, func, *args, **kwargs):
        if self.left_child:
            self.left_child.post_order(func, *args, **kwargs)
        if self.right_child:
            self.right_child.post_order(func, *args, **kwargs)
        func(self.key, *args, **kwargs)

    def in_order(self, func, *args, **kwargs):
        if self.left_child:
            self.left_child.in_order(func, *args, **kwargs)
        func(self.key, *args, **kwargs)
        if self.right_child:
            self.right_child.in_order(func, *args, **kwargs)


def pre_order(tree, func, *args, **kwargs):
    if tree:
        func(tree.get_root_val(), *args, **kwargs)
        pre_order(tree.get_left_child(), func, *args, **kwargs)
        pre_order(tree.get_right_child(), func, *args, **kwargs)


def post_order(tree, func, *args, **kwargs):
    if tree:
        post_order(tree.get_left_child(), func, *args, **kwargs)
        post_order(tree.get_right_child(), func, *args, **kwargs)
        func(tree.get_root_val(), *args, **kwargs)


def in_order(tree, func, *args, **kwargs):
    if tree is not None:
        in_order(tree.get_left_child(), func, *args, **kwargs)
        func(tree.get_root_val(), *args, **kwargs)
        in_order(tree.get_right_child(), func, *args, **kwargs)
