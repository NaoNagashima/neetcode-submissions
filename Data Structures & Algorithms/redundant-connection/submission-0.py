class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodeMap = {}
        for n in range(1, len(edges)+1):
            nodeMap[n] = []

        def dfs(node, prev):
            if visited[node]:
                return True
            visited[node] = True
            for edge in nodeMap[node]:
                if edge == prev:
                    continue
                if dfs(edge, node):
                    return True
            
            return False
        
        
        for node, edge in edges:
            nodeMap[node].append(edge)
            nodeMap[edge].append(node)
            visited = [False for _ in range(len(edges)+1)]
            if dfs(node, -1):
                return [node, edge]
        