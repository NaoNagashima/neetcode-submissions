class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for paren in s:
            if paren == "(" or paren == "{" or paren == "[":
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False

                x = stack.pop()
                if paren == ")" and x != "(":
                    return False
                elif paren == "}" and x != "{":
                    return False
                elif paren == "]" and x != "[":
                    return False
        
        if len(stack) != 0:
            return False
        return True