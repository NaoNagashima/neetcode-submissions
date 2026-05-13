"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        result = []
        seen = {}
        if not node:
            return None

        def dfs(node):
            if node in seen:
                return seen[node]
            new = Node(node.val)
            seen[node] = new
            neighbours = node.neighbors
            for neighbour in neighbours:
                new.neighbors.append(dfs(neighbour))
            return new
        
        return dfs(node)
        
                