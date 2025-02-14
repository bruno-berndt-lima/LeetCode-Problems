"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        queue = deque([node])
        clones = {node.val: Node(node.val, [])}
        while queue:
            curr_node = queue.popleft()
            curr_clone = clones[curr_node.val]

            for neighbour in curr_node.neighbors:
                if neighbour.val not in clones:
                    clones[neighbour.val] = Node(neighbour.val, [])
                    queue.append(neighbour)

                curr_clone.neighbors.append(clones[neighbour.val])
        
        return clones[node.val]
