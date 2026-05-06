class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        result = []

        if len(points) == 0:
            return []

        for x, y in points:
            distance = math.sqrt((x**2) + (y**2))
            heapq.heappush(min_heap, (distance, [x, y]))

        while k != 0:
            min_val, point = heapq.heappop(min_heap)
            result.append(point)
            k -= 1
        
        return result