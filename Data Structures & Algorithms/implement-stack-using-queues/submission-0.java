class MyStack {

    public Queue<Integer> q1;
    public Queue<Integer> q2;

    public MyStack() {
        q1 = new LinkedList<Integer>();
        q2 = new LinkedList<Integer>();
    }
    
    public void push(int x) {
        if (q2.isEmpty()){
            q1.add(x);
        } else {
            q2.add(x);
        }
    }
    
    public int pop() {
        int popped = -1;
        if (q2.isEmpty()){
            while (!q1.isEmpty()){
                 popped = q1.remove();
                if (q1.isEmpty()){
                    return popped;
                }
                q2.add(popped);
            }
            return popped;
        } else{
            while(!q2.isEmpty()){
                 popped = q2.remove();
                if (q2.isEmpty()){
                    return popped;
                }
                q1.add(popped);
            }
            return popped;
        }
    }
    
    public int top() {
        int popped = pop();
        if (q2.isEmpty()){
            q1.add(popped);
            return popped;
        }
        q2.add(popped);
        return popped;
    }
    
    public boolean empty() {
        return q1.isEmpty() && q2.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */