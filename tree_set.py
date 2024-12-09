class TreeSet:
    class Node:
        def __init__(self, val=None):
            self.val = val          
            self.left = None        
            self.right = None       
            self.size = 1           

    def __init__(self):
        self.root = None            

    def _size(self, node):
        if node is None:
            return 0
        return node.size

    def _updateSize(self, node):
        if node:
            node.size = 1 + self._size(node.left) + self._size(node.right)

    def contains(self, x):
        return self._contains(self.root, x)

    def _contains(self, node, x):
        if node is None:
            return False
        if x == node.val:
            return True
        elif x < node.val:
            return self._contains(node.left, x)
        else:
            return self._contains(node.right, x)

    def add(self, x):
        self.root = self._add(self.root, x)

    def _add(self, node, x):
        if node is None:
            return self.Node(x)
        if x == node.val:
            return node 
        elif x < node.val:
            node.left = self._add(node.left, x)
        else:
            node.right = self._add(node.right, x)
        self._updateSize(node)
        return node

    def remove(self, x):
        self.root = self._remove(self.root, x)

    def _remove(self, node, x):
        if node is None:
            return None  
        if x < node.val:
            node.left = self._remove(node.left, x)
        elif x > node.val:
            node.right = self._remove(node.right, x)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            minLargerNode = self._getMin(node.right)
            node.val = minLargerNode.val  
            node.right = self._remove(node.right, minLargerNode.val)  
        self._updateSize(node)
        return node

    def _getMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def min(self):
        if self.root is None:
            return None
        return self._getMin(self.root).val

    def max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val

    def size(self):
        return self._size(self.root)

    def count(self, lo, hi):
        return self._count(self.root, lo, hi)

    def _count(self, node, lo, hi):
        if node is None:
            return 0
        count = 0
        if lo <= node.val <= hi:
            count = 1
        if node.val > lo:
            count += self._count(node.left, lo, hi)
        if node.val < hi:
            count += self._count(node.right, lo, hi)
        return count