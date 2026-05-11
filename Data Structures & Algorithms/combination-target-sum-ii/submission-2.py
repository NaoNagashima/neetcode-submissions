class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # store any values we see and store the index so that we can have
        # duplicates that dont have the same combination
        seen = {}
        result = []
        candidates.sort()
        
        def dfs(index, curr, total) -> None:
            if total == target:
                result.append(curr.copy())
                return 
            if total > target or index >= len(candidates):
                return 
            curr.append(candidates[index])
            dfs(index + 1, curr, total + candidates[index])
            curr.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            dfs(index + 1, curr, total)
            
        
        dfs(0, [], 0)
        return result