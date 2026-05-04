# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        result = root
        while result:
            if p.val > result.val and q.val > result.val:
                result = result.right
            elif p.val < result.val and q.val < result.val:
                result = result.left
            else:
                return result

