class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        count = Counter(tasks)
        heap_freq = [-val for val in count.values()]
        heapq.heapify(heap_freq)
        
        queue = deque()
        while heap_freq or queue:
            result += 1

            if not heap_freq:
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(heap_freq)
                if count:
                    queue.append([count, result + n])
            if queue and queue[0][1] == result:
                heapq.heappush(heap_freq, queue.popleft()[0])
        return result
                


