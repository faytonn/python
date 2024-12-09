import sys


class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def count(self):
        return len(self.heap)
    
    def insert(self,x):
        self.heap.append(x)
        self._sift_up(len(self.heap) - 1)
        
    def removeSmallest(self):
        if not self.heap:
            return None

        smallest = self.heap[0]
        lastElement = self.heap.pop()
        if self.heap:
            self.heap[0] = lastElement
            self._sift_down(0)
        return smallest
    
    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
            
    def _sift_down(self, index):
        n = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
            
def read_input():
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]
    
    if not lines:
        return 0, []
    
    N = int(lines[0])
    
    employees = []
    for line in lines[1:]:
        parts = line.split()
        if len(parts) != 2:
            continue
        name, rank_str = parts
        rank = float(rank_str)
        employees.append((rank,name))
        
    return N, employees

def coffeeRoomSimulation():    
    input = sys.stdin
    
    firstLine = input.readline()
    if not firstLine:
        return
    N = int(firstLine.strip())
    
    room = PriorityQueue()
    
    for _ in range(N):
        line = input.readline()
        if not line:
            break  
        parts = line.strip().split()
        if len(parts) != 2:
            continue  
        name, rank_str = parts
        rank = float(rank_str)
        room.insert((rank, name))

    for line in input:
        parts = line.strip().split()
        if len(parts) != 2:
            continue  
        name, rank_str = parts
        rank = float(rank_str)
        smallest = room.removeSmallest()
        if smallest:
            print(f"{smallest[1]} {smallest[0]:.1f}")
            room.insert((rank, name))
        

    while room.count() > 0:
        smallest = room.removeSmallest()
        if smallest:
            print(f"{smallest[1]} {smallest[0]:.1f}")


if __name__ == "__main__":
    coffeeRoomSimulation()