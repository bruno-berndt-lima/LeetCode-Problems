# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        curr_node, parent = root, None
        while curr_node and curr_node.val != key:
            parent = curr_node
            if curr_node.val > key:
                curr_node = curr_node.left
            elif curr_node.val < key:
                curr_node = curr_node.right
            
        if not curr_node:
            return root

        # 1 - node with no children
        if not curr_node.left and not curr_node.right:
            # delete root node
            if not parent:
                return None
            
            if parent.left == curr_node:
                parent.left = None
            else:
                parent.right = None
        # 2 - node with one child
        elif not curr_node.left or not curr_node.right:
            child = curr_node.left if curr_node.left else curr_node.right

            if not parent:
                return child
            
            if parent.left == curr_node:
                parent.left = child
            else:
                parent.right = child
        # 3 - node with both children
        else :
            # find the inorder successor (smallest in th right subtree)
            successor_parent = curr_node
            successor = curr_node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # copy the inorder successor`s content to current node
            curr_node.val = successor.val
            
            # delete the inorder successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root
