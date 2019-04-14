class StructureQueue:
    def __init__(self):
        self.items = []

    def __iter__(self):
        while not self.is_empty():
            yield self.dequeue()

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
