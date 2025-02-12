# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_diff = float('inf')
        self.prev_value = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root: return self.min_diff

        self.getMinimumDifference(root.left)

        if self.prev_value is not None:
            self.min_diff = min(self.min_diff, root.val - self.prev_value)
        
        self.prev_value = root.val

        self.getMinimumDifference(root.right)

        return self.min_diff
        
        
