class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeMap = {}

        for val in range(n):
            nodeMap[val] = []

        for node, edge in edges:
            nodeMap[edge].append(node)
            nodeMap[node].append(edge)

        visited = set()
        def dfs(curr, prev):
            if nodeMap[curr] == []:
                return
            if curr in visited:
                return
            visited.add(curr)
            for edge in nodeMap[curr]:
                if edge != prev:
                    dfs(edge, curr)
            
            
        result = 0

        for val in range(n):
            if not val in visited:
                dfs(val, -1)
                result += 1
        
        return result