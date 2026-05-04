# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []

        def dfs(curr, greatest):
            if not curr:
                return None
            
            if curr.val >= greatest:
                result.append(curr.val)
                greatest = curr.val
            dfs(curr.left, greatest)
            dfs(curr.right, greatest)
        dfs(root, root.val)

        return len(result)