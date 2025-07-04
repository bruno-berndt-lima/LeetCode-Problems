class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map the key to Node

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest 

    # Remove node from list
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # Insert node at latest
    def insert(self, node: Node): 
        prev, nxt = self.latest.prev, self.latest
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev    

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
