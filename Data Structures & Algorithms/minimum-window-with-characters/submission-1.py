class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        
        for letter in t:
            countT[letter] = 1 + countT.get(letter, 0)
        
        need = len(countT)
        have = 0
        result, resultLen = [-1,-1], float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while need == have:
                if (r - l + 1) < resultLen:
                    result = [l, r]
                    resultLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return s[result[0]: result[1]+1] if resultLen != float('infinity') else ""