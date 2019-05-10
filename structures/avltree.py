from structures.binarysearchtree import BinarySearchTree
from structures.treenode import TreeNode


class AVLTree(BinarySearchTree):
    def _put(self, key, val, current_node: TreeNode, append: bool = False) -> TreeNode:
        if key == current_node.key:
            if append:
                if type(current_node.value) is not list:  # make it a list
                    current_node.value = [current_node.value, val]  # and append value to it
                else:  # already a list
                    current_node.value.append(val)  # append to the end
            else:
                current_node.value = val  # replace the value
            return current_node

        if key < current_node.key:
            if current_node.has_left_child():
                return self._put(key, val, current_node.left_child, append)
            else:
                new_node = TreeNode(key, [val] if append else val, parent=current_node)
                current_node.left_child = new_node
                self._size += 1
                self.update_balance(current_node.left_child)
                return new_node
        else:
            if current_node.has_right_child():
                return self._put(key, val, current_node.right_child, append)
            else:
                new_node = TreeNode(key, [val] if append else val, parent=current_node)
                current_node.right_child = new_node
                self._size += 1
                self.update_balance(current_node.right_child)
                return new_node

    def update_balance(self, node: TreeNode, deletion: bool = False) -> None:
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += -1 if deletion else 1
            elif node.is_right_child():
                node.parent.balance_factor -= -1 if deletion else 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, rot_root: TreeNode) -> None:
        new_root = rot_root.right_child
        rot_root.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root
        new_root.left_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + \
                                  1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + \
                                  1 + max(rot_root.balance_factor, 0)

    def rotate_right(self, rot_root: TreeNode) -> None:
        new_root = rot_root.left_child
        rot_root.left_child = new_root.right_child
        if new_root.right_child is not None:
            new_root.right_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right_child = new_root
            else:
                rot_root.parent.left_child = new_root
        new_root.right_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor - \
                                  1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - \
                                  1 + min(rot_root.balance_factor, 0)

    def rebalance(self, node: TreeNode) -> None:
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def _remove(self, current_node):
        if current_node.is_leaf():
            if current_node.is_left_child():
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
            self.update_balance(current_node, deletion=True)
            del current_node
        elif current_node.has_both_children():  # interior
            successor = current_node.successor
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
            del successor
            self.update_balance(current_node.left_child, deletion=True)  # any of children
        else:  # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                    self.update_balance(current_node.left_child, deletion=True)
                    del current_node
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                    self.update_balance(current_node.left_child, deletion=True)
                    del current_node
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.value,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                    self.update_balance(current_node.right_child, deletion=True)
                    del current_node
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                    self.update_balance(current_node.right_child, deletion=True)
                    del current_node
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.value,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)

    def __str__(self):
        return "\n".join([f"{i.balance_factor} | {i}{' (root)' if i == self.root else ''}" for i in self])
