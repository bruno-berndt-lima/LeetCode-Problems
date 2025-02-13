# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_nums = []
        def inorder_traversal(root, nums):
            if not root:
                return

            inorder_traversal(root.left, nums)
            nums.append(root.val)
            inorder_traversal(root.right, nums)

        inorder_traversal(root, sorted_nums)

        start, end = 0, len(sorted_nums) - 1

        def create_tree(nums, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            
            node = TreeNode(nums[mid], None, None)
            node.left = create_tree(nums, start, mid - 1)
            node.right = create_tree(nums, mid + 1, end)
            
            return node

        balanced_tree = create_tree(sorted_nums, start, end)

        return balanced_tree
