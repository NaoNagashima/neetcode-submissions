class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                height, index = stack.pop()
                result = max(result, height * (i - index))
                start = index
            stack.append((heights[i], start))
        
        for h, i in stack:
            result = max(result, h * (len(heights) - i))
        
        return result