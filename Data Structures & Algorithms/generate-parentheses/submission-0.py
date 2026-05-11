class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(op:int, cl:int) -> None:
            if cl == n and op == n:
                result.append("".join(stack))
                return
            
            # add a (
            if op < n:
                stack.append("(")
                backtrack(op+1, cl)
                stack.pop()
            if cl < op:
            # close )
                stack.append(")")
                backtrack(op,cl+1)
                stack.pop()
        
        backtrack(0,0)
        return result