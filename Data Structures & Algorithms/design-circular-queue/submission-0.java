class MyCircularQueue {

    class ListNode{
        int val;
        ListNode next;
        ListNode prev;

        ListNode(){}

        ListNode(int val){
            this.val = val;
        }

        ListNode(int val, ListNode next, ListNode prev){
            this.val = val;
            this.next = next;
            this.prev = prev;
        }
    }
    
    int space;
    ListNode front;
    ListNode end;

    public MyCircularQueue(int k) {
        this.space = k;
        this.front = new ListNode(-1, null, null);
        this.end = new ListNode(-1, null, this.front);
        this.front.next = end;
    }
    
    public boolean enQueue(int value) {
        if (isFull()){
            return false;
        }
        ListNode curr = new ListNode(value, end, end.prev);
        this.end.prev.next = curr;
        this.end.prev = curr;
        space--;
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()){
            return false;
        }
        ListNode pop = front.next;
        this.front.next = front.next.next;
        this.front.next.prev = front;
        space++;
        return true;
        
    }
    
    public int Front() {
        if (isEmpty()) return -1;
        return this.front.next.val;
    }
    
    public int Rear() {
        if (isEmpty()) return -1;
        return this.end.prev.val;
    }
    
    public boolean isEmpty() {
        if (this.front.next == this.end){
            return true;
        }
        return false;
    }
    
    public boolean isFull() {
        if (this.space == 0){
            return true;
        }
        return false;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */