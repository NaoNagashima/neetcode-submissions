class Solution {
    public String longestDiverseString(int a, int b, int c) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((x,y) -> y[0] - x[0]);
        if (a != 0) maxHeap.offer(new int[]{a, (int) 'a'});
        if (b != 0) maxHeap.offer(new int[]{b, (int) 'b'});
        if (c != 0) maxHeap.offer(new int[]{c, (int) 'c'});

        String result = "";
        int[] prev1 = null;
        int[] prev2 = null;
        while (!maxHeap.isEmpty()){
            int[] curr = maxHeap.poll();
            if (prev1 != null && prev2 != null && curr[1] == prev1[1] && curr[1] == prev2[1] && maxHeap.isEmpty()){
                return result;
            }
            if (prev1 != null && prev2 != null && curr[1] == prev1[1] && curr[1] == prev2[1]){
                int[] next = maxHeap.poll();
                maxHeap.offer(curr);
                curr = next;
            }

            result += ((char) curr[1]);
            curr[0]--;
            prev2 = prev1;
            prev1 = curr;
            if (curr[0] != 0){
                maxHeap.offer(curr);
            }
        }
        return result;
    }
}