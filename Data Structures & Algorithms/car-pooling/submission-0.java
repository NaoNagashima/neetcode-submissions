class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        PriorityQueue<int[]> waitingHeap = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        PriorityQueue<int[]> onHeap = new PriorityQueue<>((a,b) -> a[2] - b[2]);

        for (int[] trip: trips){
            waitingHeap.offer(trip);
        }

        int onBoard = 0;
        int distance = 0;
        while(!waitingHeap.isEmpty()){
            int[] getOn = waitingHeap.poll();
            distance = getOn[1];
            while(!onHeap.isEmpty()){
                int[] getOff = onHeap.poll();
                if (getOff[2] > distance){
                    onHeap.offer(getOff);
                    break;
                }
                onBoard -= getOff[0];
            }
            if (getOn[0] + onBoard > capacity){
                return false;
            }
            onBoard += getOn[0];
            onHeap.offer(getOn);
        }
        return true;
    }
}