class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def isPalindrome(word, l, r):
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(index) -> None:
            if index >= len(s):
                result.append(partition.copy())
                return
            
            for j in range(index, len(s)):
                if isPalindrome(s, index, j):
                    partition.append(s[index:j+1])
                    backtrack(j+1)
                    partition.pop()

                
        
        backtrack(0)

        return result