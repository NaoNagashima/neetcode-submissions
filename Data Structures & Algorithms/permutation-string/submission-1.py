class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        s1 = "".join(sorted(s1))
        for index in range(len(s2)-len(s1)+1):
            substring = s2[index:index+len(s1)]
            substring = "".join(sorted(substring))
            if s1 == substring:
                return True
            print(substring, s1)

        return False