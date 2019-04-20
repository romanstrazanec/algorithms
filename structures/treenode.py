class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

    def has_left_child(self) -> bool:
        return bool(self.left_child)

    def has_right_child(self) -> bool:
        return bool(self.right_child)

    def is_left_child(self) -> bool:
        return bool(self.parent and self.parent.left_child == self)

    def is_right_child(self) -> bool:
        return bool(self.parent and self.parent.right_child == self)

    def is_root(self) -> bool:
        return not self.parent

    def is_leaf(self) -> bool:
        return not (self.right_child or self.left_child)

    def has_any_children(self) -> bool:
        return bool(self.right_child or self.left_child)

    def has_both_children(self) -> bool:
        return bool(self.right_child and self.left_child)

    def replace_node_data(self, key, value, left_child, right_child) -> None:
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    @property
    def successor(self):
        res = None
        if self.has_right_child():
            res = self.right_child.min
        else:
            if self.parent:
                if self.is_left_child():
                    res = self.parent
                else:
                    self.parent.right_child = None
                    res = self.parent.successor
                    self.parent.right_child = self
        return res

    @property
    def predecessor(self):
        res = None
        if self.has_left_child():
            res = self.left_child.max
        else:
            if self.parent:
                if self.is_right_child():
                    res = self.parent
                else:
                    self.parent.left_child = None
                    res = self.parent.predecessor
                    self.parent.left_child = self
        return res

    @property
    def min(self):
        current = self
        # dive all the way to the left side of the tree to find min
        while current.has_left_child():
            current = current.left_child
        return current

    @property
    def max(self):
        current = self
        # dive all the way to the right side of the tree to find max
        while current.has_right_child():
            current = current.right_child
        return current

    def splice_out(self) -> None:
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    def __str__(self):
        return f"{self.key}: {self.value}"

    def __repr__(self):
        return f"TreeNode({self.key}, {self.value})"
