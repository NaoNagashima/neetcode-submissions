class MyHashSet {

    public ArrayList<Integer> hashSet;
    public MyHashSet() {
        this.hashSet = new ArrayList<>();
    }
    
    public void add(int key) {
        if (!contains(key)){
            this.hashSet.add(key);
        }
    }
    
    public void remove(int key) {
        this.hashSet.remove(Integer.valueOf(key));
    }
    
    public boolean contains(int key) {
        return this.hashSet.contains(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */