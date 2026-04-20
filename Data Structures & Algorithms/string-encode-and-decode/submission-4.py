class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += '!'+str(len(s)) +"!" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            i += 1
            str_count = ""
            while s[i] != "!":
                str_count += s[i]
                i += 1
            i += 1
            count = int(str_count)
            word = ""
            while count > 0:
                word += s[i]
                count -= 1
                i += 1
            result.append(word)
        return result
