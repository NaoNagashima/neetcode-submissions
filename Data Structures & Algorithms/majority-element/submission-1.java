class Solution {
    public int majorityElement(int[] nums) {
        HashMap <Integer, Integer> occurMap = new HashMap<>();
        int limit = nums.length / 2;
        if (nums.length == 1){
            return nums[0];
        }
        for (int n: nums){
            if (occurMap.containsKey(n)){
                int newOccur = occurMap.get(n) + 1;
                occurMap.put(n, newOccur);
                if (newOccur > limit){
                    return n;
                }
            } else {
                occurMap.put(n, 1);
            }
        }
        return -1;
    }
}