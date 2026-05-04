# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        low, high = float('inf'), -float('inf')

        def dfs(curr, low, high):
            if not curr:
                return True
            
            if curr.val < low and curr.val > high:
                left = True
                right = True
                if curr.left:
                    left = dfs(curr.left, curr.val, high)
                if curr.right:
                    right = dfs(curr.right, low, curr.val)
                return left and right
            return False
        
        return dfs(root, low, high)
