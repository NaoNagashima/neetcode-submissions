class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first = 0
        second = 1
        nums.sort()

        while second < len(nums):
            if nums[first] == nums[second]:
                return nums[first]
            first += 1
            second += 1
        
        return 0
        