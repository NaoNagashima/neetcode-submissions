class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        current = 1
        nums.sort()

        if nums == []:
            return 0
        elif len(nums) == 1:
            return 1
        
        index = 1

        while index < len(nums):
            if nums[index] == nums[index-1]+1:
                current += 1
            if nums[index] > nums[index-1]+1:
                if current > longest:
                    longest = current
                current = 1
            index += 1
        if current > longest:
            return current
        return longest
