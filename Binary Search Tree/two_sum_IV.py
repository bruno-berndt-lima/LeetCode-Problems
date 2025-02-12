# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = deque([root])
        nums_set = set()
        while queue:
            node = queue.popleft()
            
            diff = k - node.val
            if diff in nums_set:
                return True
            else:
                nums_set.add(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
    
        return False
