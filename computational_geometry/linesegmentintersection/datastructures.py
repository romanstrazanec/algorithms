class Queue:
  def __init__(self):
    self.items = []

  def __len__(self):
    return len(self.items)

  def __iter__(self):
    return iter(self.items)

  def __next__(self):
    return next(self.items)

  def add(self, *items):
    for item in items:
      self.items.insert(0, item)

  def pop(self):
    return self.items.pop()

  def contains(self, item):
    return item in self.items

  def __str__(self):
    return str(self.items)


class BinarySearchTree:
  def __init__(self, item=None):
    self.item = item
    self.left = None
    self.right = None

  def print(self):
    if self.left:
      self.left.print()

    print(self.item)

    if self.right:
      self.right.print()

  def insert(self, item):
    if self.item is None:
      self.item = item
    else:
      if item > self.item:
        if self.right is None:
          self.right = BinarySearchTree(item)
        else:
          self.right.insert(item)
      elif item < self.item:
        if self.left is None:
          self.left = BinarySearchTree(item)
        else:
          self.left.insert(item)

  def search(self, item):
    if self.item == item:
      return self
    if self.right and item > self.item:
      return self.right.search(item)
    if self.left and item < self.item:
      return self.left.search(item)

  def delete(self, item):
    if self is None or not self.search(item):
      return self
    if item < self.item:
      self.left = self.left.delete(item)
    elif item > self.item:
      self.right = self.right.delete(item)
    else:
      if self.left is None:
        temp = self.right
        self = None
        return temp

      elif self.right is None:
        temp = self.left
        self = None
        return temp

      temp = self.right.min()
      self.item = temp.item
      self.right = self.right.delete(temp.item)

    return self

  def min(self):
    current = self
    while current.left is not None:
      current = current.left
    return current

  def max(self):
    current = self
    while current.right is not None:
      current = current.right
    return current
