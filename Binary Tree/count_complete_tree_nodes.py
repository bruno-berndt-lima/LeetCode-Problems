# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        n_nodes = 0
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            n_nodes += 1
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)

        return n_nodes
