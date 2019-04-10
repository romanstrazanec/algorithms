class BinaryHeap:
    def __init__(self, alist=None):
        if alist is None:
            self.heap_list = [0]
            self.current_size = 0
        else:
            self.build_heap(alist)

    def perc_up(self, i):
        p = i // 2
        while p > 0:
            if self.heap_list[i] < self.heap_list[p]:
                self.heap_list[i], self.heap_list[p] = self.heap_list[p], self.heap_list[i]
            i = p
            p //= 2

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def min_child(self, i):
        i *= 2
        return i if i + 1 > self.current_size else i if self.heap_list[i] < self.heap_list[i + 1] else i + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i -= 1
