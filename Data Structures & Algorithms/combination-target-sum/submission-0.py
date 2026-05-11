class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def subSum(index, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if total > target:
                return []
            if index >= len(nums):
                return []
            # recurse with itself in it
            subSum(index, [nums[index]] + curr, total + nums[index])

            # recurse without itself in it
            subSum(index + 1, curr, total)
            
            
        
        subSum(0, [], 0)
        return result