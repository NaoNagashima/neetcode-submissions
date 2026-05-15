class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap = {}

        for val in range(n):
            nodeMap[val] = []
        
        for node, edge in edges:
            nodeMap[node].append(edge)
            nodeMap[edge].append(node)        
        
        visited = set()
        print(nodeMap)
        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for edge in nodeMap[curr]:
                if edge != prev:
                    if not dfs(edge, curr):
                        return False
            return True
        
        for val in range(n):
            visited = set()
            if not dfs(val, -1):
                return False
            if len(visited) == n:
                return True
        
        return False