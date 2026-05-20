class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        Set<Integer> window = new HashSet<>();
        int left = 0;
        int sum = 0;
        int minSize = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++){
            sum += nums[right];
            if (sum >= target){
                while (sum >= target){
                    minSize = Math.min(minSize, right - left + 1);
                    sum -= nums[left];
                    left++;
                }
            }
        }
        if (minSize != Integer.MAX_VALUE){
            return minSize;
        }
        return 0;
    }
}