# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [[2] [4 5]]
# [[3] [6 7]]

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        def dfs(node, depth):
            if not node:
                return None
            
            if len(result) == depth:
                result.append([])
            
            result[depth].append(node.val)
            depth += 1
            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)

        return result
            