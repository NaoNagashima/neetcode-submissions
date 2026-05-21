class Solution {
    public String reorganizeString(String s) {
        int[] freqMap = new int[26];
        for (int i = 0; i < s.length(); i++){
            freqMap[s.charAt(i) - 'a']++;
        }
        
        PriorityQueue<int[]> mostFreq = new PriorityQueue<>((a,b) -> b[0] - a[0]);

        for (int i = 0; i < 26; i++){
            if (freqMap[i] > 0){
                mostFreq.offer(new int[]{freqMap[i], i});
            }
        }

        int[] prev = null;
        String result = "";
        while (!mostFreq.isEmpty() || prev != null){
            if (prev != null && mostFreq.isEmpty()){
                return "";
            }
            int[] curr = mostFreq.poll();
            result += ((char)(curr[1] + 'a'));
            System.out.println((char)(curr[1] + 'a'));
            curr[0]--;
            if (prev != null){
                mostFreq.offer(prev);
                prev = null;
            }
            if (curr[0] > 0){
                prev = curr;
            }
        }
        return result;
    }
}