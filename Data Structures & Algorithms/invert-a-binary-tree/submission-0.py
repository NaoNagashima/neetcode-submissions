# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        elif root.left == None and root.right == None:
            return root
        elif root.left == None and root.right != None:
            right = self.invertTree(root.right)
            root.right = None
            root.left = right
            return root
        elif root.left != None and root.right == None:
            left = self.invertTree(root.left)
            root.left = None
            root.right = left
            return root
        elif root.left != None and root.right != None:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left
            return root
