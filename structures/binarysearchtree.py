from typing import Optional

from structures.treenode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    @property
    def length(self) -> int:
        return self._size

    def __len__(self):
        return self._size

    def __iter__(self):
        return iter(self.root) if self.root is not None else iter([])

    def put(self, key, val) -> None:
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self._size = 1

    def append(self, key, val) -> None:
        """Same as put but appends the value to the key if it exists or creates a list with the value if not"""
        if self.root:
            self._put(key, val, self.root, append=True)
        else:
            self.root = TreeNode(key, [val])
            self._size = 1

    def _put(self, key, val, current_node, append: bool = False) -> None:
        if key == current_node.key:  # if key already exists, replace value
            if append:
                if type(current_node.value) is not list:  # make it a list
                    current_node.value = [current_node.value, val]  # and append value to it
                else:  # already a list
                    current_node.value.append(val)  # append to the end
            else:
                current_node.value = val  # replace the value
            return

        if key < current_node.key:  # go left
            if current_node.has_left_child():  # handle left tree
                self._put(key, val, current_node.left_child, append)
            else:  # set left tree node
                current_node.left_child = TreeNode(key, [val] if append else val, parent=current_node)
                self._size += 1
        else:  # go right
            if current_node.has_right_child():  # handle right tree
                self._put(key, val, current_node.right_child, append)
            else:  # set right tree node
                current_node.right_child = TreeNode(key, [val] if append else val, parent=current_node)
                self._size += 1

    def __setitem__(self, k, v):
        """bst[k] = v"""
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            return res.value if res else None

    def _get(self, key, current_node: TreeNode) -> Optional[TreeNode]:
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        """bst[key]"""
        return self.get(key)

    def __contains__(self, key):
        """key in bst"""
        return True if self._get(key, self.root) else False

    def delete(self, key):
        if self._size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self._size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self._size == 1 and self.root.key == key:
            self.root = None
            self._size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        """del bst[key]"""
        self.delete(key)

    @staticmethod
    def remove(current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():  # interior
            successor = current_node.successor
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:  # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.value,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.value,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)

    @property
    def min(self) -> Optional[TreeNode]:
        if self.root:
            return self.root.min

    @property
    def max(self) -> Optional[TreeNode]:
        if self.root:
            return self.root.max

    def left_of(self, key):
        pass

    def right_of(self, key):
        pass

    def __str__(self):
        return "\n".join([str(i) for i in self])

    def __repr__(self):
        return str(self)
