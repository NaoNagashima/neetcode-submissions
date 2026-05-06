class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        result = 0
        while k != 0:
            k -= 1
            result = -heapq.heappop(nums)
            
        return result
            