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

    def preorder(self, func, *args, **kwargs):
        func(self.key, *args, **kwargs)
        if self.left_child:
            self.left_child.preorder(func, *args, **kwargs)
        if self.right_child:
            self.right_child.preorder(func, *args, **kwargs)

    def postorder(self, func, *args, **kwargs):
        if self.left_child:
            self.left_child.postorder(func, *args, **kwargs)
        if self.right_child:
            self.right_child.postorder(func, *args, **kwargs)
        func(self.key, *args, **kwargs)

    def inorder(self, func, *args, **kwargs):
        if self.left_child:
            self.left_child.inorder(func, *args, **kwargs)
        func(self.key, *args, **kwargs)
        if self.right_child:
            self.right_child.inorder(func, *args, **kwargs)


def preorder(tree, func, *args, **kwargs):
    if tree:
        func(tree.get_root_val(), *args, **kwargs)
        preorder(tree.get_left_child(), func, *args, **kwargs)
        preorder(tree.get_right_child(), func, *args, **kwargs)


def postorder(tree, func, *args, **kwargs):
    if tree:
        postorder(tree.get_left_child(), func, *args, **kwargs)
        postorder(tree.get_right_child(), func, *args, **kwargs)
        func(tree.get_root_val(), *args, **kwargs)


def inorder(tree, func, *args, **kwargs):
    if tree is not None:
        inorder(tree.get_left_child(), func, *args, **kwargs)
        func(tree.get_root_val(), *args, **kwargs)
        inorder(tree.get_right_child(), func, *args, **kwargs)
