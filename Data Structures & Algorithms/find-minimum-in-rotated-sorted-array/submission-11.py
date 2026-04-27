class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        result = float('inf')

        # 4 1 2 3
        # 3 4 1 2
        # 4 5 6 0 1 2 3
        # if mid is less than left than at a certain point the array reset
        # 3 4 5 6 0 1 2

        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        mid = 0
        result = nums[0]
        while left <= right:
            mid = (left + right) // 2

            if nums[left] < nums[right]:
                return min(result, nums[left])
            result = min(result, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return result
