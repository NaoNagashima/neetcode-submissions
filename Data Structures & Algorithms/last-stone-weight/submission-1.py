class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while stones:
            if len(stones) >= 2:
                first = heapq.heappop(stones)
                second = heapq.heappop(stones)
                if abs(first - second) != 0:
                    heapq.heappush(stones, first - second)
            else:
                return -1 * stones[0]
        return 0