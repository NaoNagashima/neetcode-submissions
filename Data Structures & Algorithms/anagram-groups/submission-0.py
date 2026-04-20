class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            sorted_copy = sorted(word)
            sorted_copy = "".join(sorted_copy)
            if sorted_copy not in result:
                result[sorted_copy] = [word]
            else:
                result[sorted_copy].append(word)
        
        return list(result.values())