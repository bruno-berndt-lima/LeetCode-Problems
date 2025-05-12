# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    parent[node.left.val] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right.val] = node
                    queue.append(node.right)

        visited = {}
        queue = deque([target])
        while k > 0 and queue:
            for i in range(len(queue)):
                node = queue.popleft()
                visited[node.val] = True

                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                if node.val in parent and parent[node.val].val not in visited:
                    queue.append(parent[node.val])

            k -= 1

        result = []
        while queue:
            result.append(queue.popleft().val)

        return result
