class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10001)]
    
    def hash_func(self, key: int):
        index = key % len(self.set)
        return index

    def add(self, key: int) -> None:
        curr = self.set[self.hash_func(key)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next

        curr.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        curr = self.set[self.hash_func(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next        

    def contains(self, key: int) -> bool:
        curr = self.set[self.hash_func(key)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next 
        
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
