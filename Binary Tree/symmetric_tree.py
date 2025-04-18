# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(node_l, node_r):
            if not node_l and not node_r:
                return True

            if not node_l or not node_r:
                return False

            return node_l.val == node_r.val and is_mirror(node_l.left, node_r.right) and is_mirror(node_l.right, node_r.left)

        return is_mirror(root.left, root.right)
