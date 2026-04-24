class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We want to find which cars would catch up to the previous cars
        # the cars that do catch up can be popped from the stack
        # keep the higher position car

        # (0, 1) (1, 2) (4, 2) (7, 1)

        lst = [(p,s) for p, s in zip(position, speed)]
        lst.sort(reverse=True)
        stack = []

        for p, s in lst:
            time = (target - p ) / s
            if len(stack) != 0:
                if stack[-1] < time:
                    stack.append(time)
            else:
                stack.append(time)
        
        return len(stack)