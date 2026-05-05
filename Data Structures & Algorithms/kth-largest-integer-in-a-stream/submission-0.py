class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = []
        self.k = k
        for n in nums:
            heapq.heappush(self.arr, n)  
            if len(self.arr) > self.k:
                heapq.heappop(self.arr)      

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
        return self.arr[0]
        
