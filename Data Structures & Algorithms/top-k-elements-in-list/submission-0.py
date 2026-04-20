class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(1, len(nums)+1):
            freq[i] = []
        
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

        for a,v in seen.items():
            freq[v].append(a)

        i = len(nums)
        j = 0
        res = []
        while i > 0:
            if freq[i] != []:
                r = freq[i].pop()
                res.append(r)
                j += 1
                if j == k:
                    return res
            else:
                i -= 1


        

        