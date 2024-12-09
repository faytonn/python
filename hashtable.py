import sys


def my_hash(s):
    h = 0
    for c in s:
        h = (h * 1_000_003 + ord(c)) % (2 ** 32)
    return h 

class Node:
    def __init__(self, key, value, nextNode = None):
        self.key = key
        self.value = value
        self.next = nextNode
        
class HashMap:
    def __init__(self):
        self.num_buckets = 5
        self.buckets = [None] * self.num_buckets
        self.size = 0
        
    def set(self, key, value):
        if(self.size + 1) / self.num_buckets > 4:
            self._resize()
            
        index = my_hash(key) % self.num_buckets
        head = self.buckets[index]
        
        current = head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
            
        new_node = Node(key, value, head)
        self.buckets[index] = new_node
        self.size += 1
        

    def get(self, key):
        index = my_hash(key) % self.num_buckets
        current = self.buckets[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
            
    def remove(self, key):
        index = my_hash(key) % self.num_buckets
        current = self.buckets[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def _resize(self):
         new_num_buckets = self.num_buckets * 2
         print(f"resizing to {new_num_buckets} buckets")
         new_buckets = [None] * new_num_buckets

         for i in range(self.num_buckets):
            current = self.buckets[i]
            while current is not None:
                index = my_hash(current.key) % new_num_buckets
                new_node = Node(current.key, current.value, new_buckets[index])
                new_buckets[index] = new_node
                current = current.next
                
         self.num_buckets = new_num_buckets
         self.buckets = new_buckets
         
def isLetter(char):
        lowercaseLetters = 'qwertyuiopasdfghjklzxcvbnm'
        capitalLetters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        return char in lowercaseLetters or char in capitalLetters
    
def main():
        frequencyMap = HashMap()
        lines = []
        
        for line in sys.stdin:
            line = line.strip('\n')
            if line == '== END ==':
                break
            lines.append(line)
            
        text = "\n".join(lines)
        
        currentWord = ""
        for char in text:
            if isLetter(char):
                currentWord += char
            else:
                if currentWord:
                    w = currentWord.lower()
                    count = frequencyMap.get(w)
                    if count is None:
                        frequencyMap.set(w,1)
                    else:
                        frequencyMap.set(w, count + 1)
                        
                    currentWord = ""
                    
        if currentWord:
             w = currentWord.lower()
             count = frequencyMap.get(w)
             if count is None:
                frequencyMap.set(w,1)
             else:
                frequencyMap.set(w, count + 1)
        
        print(f"unique words = {frequencyMap.size}")
        
        for query_line in sys.stdin:
            query = query_line.strip()
            if not query:
                continue
            query_lower = query.lower()
            count = frequencyMap.get(query_lower)
            if count is not None:
                print(f"{query_lower} {count}")
                frequencyMap.remove(query_lower)
            else:
                print(f"{query_lower} None")
                
if __name__ == "__main__":
    main()

 