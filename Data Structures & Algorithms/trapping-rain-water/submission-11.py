class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        result = 0

        start = 0
        end = len(height) - 1
        max_start = height[start]
        max_end = height[end]
        
        while start < end:
            if height[start] < height[end]:
                start += 1
                max_start = max(max_start, height[start])
                result += max_start - height[start]
            else:
                end -= 1
                max_end = max(max_end, height[end])
                result += max_end - height[end]
        return result