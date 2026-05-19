class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int a: asteroids){
            while (!stack.isEmpty() && stack.peek() > 0 && a < 0){
                if (stack.peek() < -a){
                    stack.pop();
                } else if (stack.peek() > -a){
                    a = 0;
                } else{
                    stack.pop();
                    a = 0;
                }
            }

            if (a != 0){
                stack.push(a);
            }
        }

        return stack.stream().mapToInt(Integer::intValue).toArray();

    }
}