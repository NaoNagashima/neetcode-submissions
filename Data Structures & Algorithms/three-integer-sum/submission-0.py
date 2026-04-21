class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        nums.sort()

        for i in range(len(nums)):
            copy = nums.copy()
            copy.pop(i)

            start = 0
            end = len(copy)-1

            while start < end:
                l = [nums[i], copy[start], copy[end]]
                l.sort()
                if copy[start] + copy[end] + nums[i] == 0 and l not in result:
                    result.append(l)
                elif copy[start] + copy[end] + nums[i] < 0:
                    start += 1
                else:
                    end -= 1
        
        return result