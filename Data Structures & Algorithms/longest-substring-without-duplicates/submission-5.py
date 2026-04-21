class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        first = 0
        second = 1
        longest = 0

        while second < len(s):
            if s[second] not in s[first:second]:
                second += 1
                if second - first > longest:
                    longest = second - first
            else:
                first += 1
            
        return longest