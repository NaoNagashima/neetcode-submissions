# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(root) -> int:
            if root == None:
                return 0
            elif root.left == None and root.right == None:
                return 1
            
            leftpath = dfs(root.left)
            rightpath = dfs(root.right)
            
            self.result = max(self.result, leftpath + rightpath)

            if leftpath > rightpath:
                return leftpath + 1
            return rightpath + 1
    
        dfs(root)
        return self.result