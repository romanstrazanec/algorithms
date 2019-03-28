class BinaryHeap:
    def __init__(self, alist=[]):
        if alist == []:
            self.heapList = [0]
            self.currentSize = 0
        else:
            self.buildHeap(alist)

    def percUp(self, i):
        p = i // 2
        while p > 0:
            if self.heapList[i] < self.heapList[p]:
                self.heapList[i], self.heapList[p] = self.heapList[p], self.heapList[i]
            i = p
            p //= 2

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def minChild(self, i):
        i *= 2
        return i if i + 1 > self.currentSize else i if self.heapList[i] < self.heapList[i+1] else i + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1
