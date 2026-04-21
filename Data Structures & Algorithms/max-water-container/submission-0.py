class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        max_area = 0
        
        while start < end:
            width = end - start
            start_height = heights[start]
            end_height = heights[end]
            min_height = start_height if start_height < end_height else end_height
            if width * min_height > max_area:
                max_area = width * min_height
            
            if start_height < end_height:
                start += 1
            else:
                end -= 1
        
        return max_area