"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {None : None}
        
        current_node = head
        while current_node:
            copy = Node(current_node.val)
            original_to_copy[current_node] = copy
            current_node = current_node.next

        current_node = head
        while current_node:
            copy = original_to_copy[current_node]
            copy.next = original_to_copy[current_node.next]
            copy.random = original_to_copy[current_node.random]
            current_node = current_node.next

        return original_to_copy[head]
