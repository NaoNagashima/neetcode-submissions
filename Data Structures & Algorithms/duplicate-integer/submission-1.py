class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        n = 1

        while n < len(nums):
            if nums[n] == nums[n-1]:
                return True
            n += 1
        
        return False