class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        copy = nums.copy()
        copy.sort()

        start = 0
        end = len(copy) - 1

        while start < end:
            if copy[start] + copy[end] == target:
                start_index = nums.index(copy[start])
                end_index = nums.index(copy[end])
                if start_index != end_index:
                    result = [start_index, end_index]
                    result.sort()
                    return result
                nums[start_index] = copy[start] - 1
                return [start_index, nums.index(copy[start])]
            elif copy[start] + copy[end] < target:
                start += 1
            else:
                end -= 1