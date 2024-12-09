class CircularQueue:
    def __init__(self, size):
        self.a = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0
        self._count = 0
        self.sum = 0

    def enqueue(self, n):
        if (self.tail + 1) % self.size == self.head:
            new_size = self.size * 2
            new_a = [None] * new_size
            for i in range(self._count):
                new_a[i] = self.a[(self.head + i) % self.size]
            self.a = new_a
            self.size = new_size
            self.head = 0
            self.tail = self._count
            print(f"Resized to {self.size} elements")
        self.a[self.tail] = n
        self.tail = (self.tail + 1) % self.size
        self._count += 1
        self.sum += n

    def dequeue(self):
        val = self.a[self.head]
        self.a[self.head] = None
        self.head = (self.head + 1) % self.size
        self._count -= 1
        self.sum -= val
        return val

    def count(self):
        return self._count

    def avg(self):
        return self.sum / self._count