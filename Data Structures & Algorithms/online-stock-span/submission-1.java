class StockSpanner {

    class Entry{
        int value;
        int span;
        
        Entry(int value, int span){
            this.value = value;
            this.span = span;
        }
    }
    private Stack<Entry> stack;

    public StockSpanner() {
        stack = new Stack<Entry>();
    }
    
    public int next(int price) {
        if (stack.isEmpty()){
            stack.push(new Entry(price, 1));

            return 1;
        } else {
            int span = 1;
            while (!stack.isEmpty() && stack.peek().value <= price){
                Entry e = stack.pop();
                span = span + e.span;
            }
            Entry result = new Entry(price, span);
            stack.push(result);
            return span;
        }
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */