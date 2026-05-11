class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(curr, whats_left):
            if whats_left == []:
                result.append(curr)
                return
            
            index = 0
            temp = whats_left.copy()
            while index < len(temp):
                popped = temp.pop(index)
                dfs(curr + [popped], temp)
                temp = whats_left.copy()
                index += 1
        
        dfs([], nums)
        return result