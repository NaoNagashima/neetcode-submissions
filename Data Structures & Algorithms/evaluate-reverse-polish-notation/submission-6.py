class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                arg2 = stack.pop()
                arg1 = stack.pop()
                if t == "+":
                    stack.append(arg1 + arg2)
                elif t == "-":
                    stack.append(arg1 - arg2)
                elif t == "*":
                    stack.append(arg1 * arg2)
                elif t == "/":
                    stack.append(int(float(arg1)/arg2))
                print(stack[-1])
            else:
                stack.append(int(t)) 
    
        return stack[0]