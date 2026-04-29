class TimeMap:

    def __init__(self):
        self.keys = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = [(0, "")]
        self.keys[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        times = sorted(self.keys[key])

        left = 0
        right = len(times)-1
        mid = 0
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if times[mid][0] <= timestamp:
                left = mid + 1
                result = times[mid][1]
            else:
                right = mid - 1
        print(mid, left, right, times)
        return result
