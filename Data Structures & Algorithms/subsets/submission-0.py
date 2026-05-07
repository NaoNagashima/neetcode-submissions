class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        first_element = nums[0]
        rest_elements = nums[1:]

        rest_subset = self.subsets(rest_elements)
        result = []
        for rest in rest_subset:
            result.append(rest)
            result.append(rest+[first_element])
        
        return result