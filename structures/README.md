# Data Structures

Implemented algorithms from two topics of interactivepython website:

- [Basic Data Structures](http://interactivepython.org/runestone/static/pythonds/BasicDS/toctree.html)
- [Trees and Tree Algorithms](http://interactivepython.org/runestone/static/pythonds/Trees/toctree.html)

## Stack

A stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This end is commonly referred to as the “top.” The end opposite the top is known as the “base.”

Methods:

- is_empty -> True if empty
- push(item) -> pushes item to the top
- pop -> gets item at the top and remove it
- peek -> gets item at the top without removing it
- size -> gets size

## Queue

A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.” As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.

Methods:

- is_empty -> True if empty
- enqueue(item) -> adds item to the end
- dequeue -> gets item from the front and remove it
- size -> gets size

## Deque

A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a deque different is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rear. Likewise, existing items can be removed from either end.

Methods:

- is_empty -> True if empty
- add_front(item) -> adds item to the front
- add_rear(item) -> adds item to the back
- remove_front -> gets and remove item from the front
- remove_rear -> gets and remove item from the back
- size -> gets size

## List

A list is a collection of items where each item holds a relative position with respect to the others.

Methods:

- is_empty -> True if empty
- add(item) -> adds item to the end
- size -> gets size
- search(item) -> checks if item in list
- remove(item) -> removes item from the list

## Binary Tree

A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the following properties:

- One node of the tree is designated as the root node.
- Every node n, except the root node, is connected by an edge from exactly one other node p, where p is the parent of n.
- A unique path traverses from the root to each node.
- If each node in the tree has a maximum of two children, we say that the tree is a binary tree.

Methods:

- insert_left(item) -> inserts item to the left of the current tree
- insert_right(item) -> inserts item to the right of the current tree
- get_left_child -> gets the left child
- get_right_child -> gets the right child
- set_root_val(item) -> sets the root value
- get_root_val -> gets the root value

Performing a function on the whole tree with different order:

- preorder(func, *args, **kwargs)
- postorder(func, *args, **kwargs)
- inorder(func, *args, **kwargs)

These functions can be used as a part of an instance or as a part of the module with the tree as a first parameter.

