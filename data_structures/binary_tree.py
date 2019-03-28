class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self, func, *args, **kwargs):
        func(self.key, *args, **kwargs)
        if self.leftChild:
            self.leftChild.preorder(func, *args, **kwargs)
        if self.rightChild:
            self.rightChild.preorder(func, *args, **kwargs)

    def postorder(self, func, *args, **kwargs):
        if self.leftChild:
            self.leftChild.postorder(func, *args, **kwargs)
        if self.rightChild:
            self.rightChild.postorder(func, *args, **kwargs)
        func(self.key, *args, **kwargs)

    def inorder(self, func, *args, **kwargs):
        if self.leftChild:
            self.leftChild.inorder(func, *args, **kwargs)
        func(self.key, *args, **kwargs)
        if self.rightChild:
            self.rightChild.inorder(func, *args, **kwargs)


def preorder(tree, func, *args, **kwargs):
    if tree:
        func(tree.getRootVal(), *args, **kwargs)
        preorder(tree.getLeftChild(), func, *args, **kwargs)
        preorder(tree.getRightChild(), func, *args, **kwargs)


def postorder(tree, func, *args, **kwargs):
    if tree:
        postorder(tree.getLeftChild(), func, *args, **kwargs)
        postorder(tree.getRightChild(), func, *args, **kwargs)
        func(tree.getRootVal(), *args, **kwargs)


def inorder(tree, func, *args, **kwargs):
    if tree != None:
        inorder(tree.getLeftChild(), func, *args, **kwargs)
        func(tree.getRootVal(), *args, **kwargs)
        inorder(tree.getRightChild(), func, *args, **kwargs)
