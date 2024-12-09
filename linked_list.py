
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    

class LinkedList:
    def __init__(self, vals):
        self.head = None
        current = None
        for val in vals:
            new_node = Node(val)
            if not self.head:
                self.head = new_node
            else:
                current.next = new_node
            current = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def len(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get(self, n):
        current = self.head
        for _ in range(n):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current is None:
            raise IndexError("Index out of bounds")
        return current.val

    def has(self, x):
        current = self.head
        while current:
            if current.val == x:
                return True
            current = current.next
        return False

    def delete(self, x):
        if not self.head:
            return
        if self.head.val == x:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.val == x:
                current.next = current.next.next
                return
            current = current.next
    
    def rotate(self):
        if not self.head or not self.head.next:
            return
        prev, last = None, self.head
        while last.next:
            prev = last
            last = last.next
        if prev:
            prev.next = None
        last.next = self.head
        self.head = last

    def starts_with(self, m):
        p, q = self.head, m.head
        while q:
            if not p or p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True
    
    def contains(self, m):
        p = self.head
        while p:
            if self.starts_with(m):
                return True
            p = p.next
        return False

    def ends_with(self, m):
        len_self = self.len()
        len_m = m.len()
        if len_m > len_self:
            return False
        skip = len_self - len_m
        p, q = self.head, m.head
        for _ in range(skip):
            p = p.next
        while q:
            if not p or p.val != q.val:
                return False
            p = p.next
            q = q.next
       return True
