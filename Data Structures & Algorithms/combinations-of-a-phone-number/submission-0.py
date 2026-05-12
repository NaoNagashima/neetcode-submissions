class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitmap = {
            "2":["a","b","c"]
            ,"3":["d","e","f"]
            ,"4":["g","h","i"]
            ,"5":["j","k","l"]
            ,"6":["m","n","o"]
            ,"7":["p","q","r","s"]
            ,"8":["t","u","v"]
            ,"9":["w","x","y","z"]}
        
        def backtrack(i, curr):
            if i >= len(digits):
                if curr:
                    result.append(curr)
                return
            
            digitChars = digitmap[digits[i]]
            for letter in digitChars:
                curr += letter
                backtrack(i+1, curr)
                curr = curr[:-1]
        
        backtrack(0, "")

        return result
            