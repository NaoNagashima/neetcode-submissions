class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, curr):
            if index == len(nums):
                result.append(curr.copy())
                return
            
            curr.append(nums[index])
            backtrack(index + 1, curr)
            curr.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            
            backtrack(index+1, curr)
    
        backtrack(0, [])

        return result