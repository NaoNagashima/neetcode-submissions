class Solution {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) != ']'){
                stack.push(String.valueOf(s.charAt(i)));
            } else {
                StringBuilder subset = new StringBuilder();

                while(!stack.peek().equals("[")){
                    subset.insert(0, stack.pop());
                }
                StringBuilder numString = new StringBuilder();
                stack.pop();
                while(!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))){
                    numString.insert(0, stack.pop());
                }
                int num = Integer.parseInt(numString.toString());
                String repeated = subset.toString().repeat(num);
                stack.push(repeated);
            }
        }
        String result = "";
        while (!stack.isEmpty()){
            result = stack.pop() + result;
        }
        return result;
    }
}