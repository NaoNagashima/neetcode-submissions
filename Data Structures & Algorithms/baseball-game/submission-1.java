class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();

        for (String s: operations){
            if (s.equals("+")){
                 int val2 = stack.pop();
                 int val1 = stack.pop();
                 stack.push(val1);
                 stack.push(val2);
                 stack.push(val1 + val2);
            } else if (s.equals("D")){
                int val1 = stack.peek();
                stack.push(val1 * 2);
            } else if (s.equals("C")){
                int val1 = stack.pop();
            } else {
                stack.push(Integer.parseInt(s));
            }
        }

        int result = 0;
        while(!stack.isEmpty()){
            result = result + stack.pop();
        }
        return result;
    }
}