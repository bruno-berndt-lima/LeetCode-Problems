# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)

        curr_node = root
        new_node = TreeNode(val, None, None)

        while curr_node:
            if curr_node.val < val:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = new_node
                    break
            else:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = new_node
                    break

        return root
