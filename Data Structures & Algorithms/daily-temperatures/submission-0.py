class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i],i])
            else:
                while len(stack) != 0:
                    if stack[-1][0] < temperatures[i]:
                        t, j = stack.pop()
                        result[j] = i - j
                    else:
                        break
                stack.append([temperatures[i], i])
        return result
