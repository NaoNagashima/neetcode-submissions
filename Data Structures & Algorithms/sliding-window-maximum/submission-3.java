class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int right = 0;
        int[] result = new int[nums.length-k+1];
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int left = 0; left < nums.length - k + 1; left++){
            while (right - left != k){
                pq.offer(nums[right]);
                right++;
            }
            // System.out.println(pq.toString());
            result[left] = pq.peek();
            int size = pq.size();
            PriorityQueue<Integer> tempq = new PriorityQueue<>(Collections.reverseOrder());
            while(true){
                int temp = pq.poll();
                if (temp == nums[left]){
                    break;
                }
                tempq.offer(temp);
            }
            while(!tempq.isEmpty()){
                pq.offer(tempq.poll());
            }
        }
        return result;
    }
}
