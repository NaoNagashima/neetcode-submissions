class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        forward = []
        prod = 1
        for i in nums:
            prod *= i
            forward.append(prod)
        
        backward = []
        prod = 1
        nums.reverse()
        for j in nums:
            prod *= j
            backward.append(prod)
        backward.reverse()

        for n in range(len(nums)):
            if n == 0:
                result.append(backward[n+1])
            elif n == len(nums)-1:
                result.append(forward[n-1])
            else:
                result.append(forward[n-1] * backward[n+1])
        return result