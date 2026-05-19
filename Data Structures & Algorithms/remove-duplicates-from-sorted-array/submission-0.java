class Solution {
    public int removeDuplicates(int[] nums) {
        HashSet<Integer> numMap = new HashSet<>();
        int first = 0;
        int second = 0;
        int result = 0;

        while(second < nums.length){
            if (numMap.contains(Integer.valueOf(nums[first]))){
                if (numMap.contains(Integer.valueOf(nums[second]))){
                    second++;
                } else{
                    nums[first] = nums[second];
                    numMap.add(nums[first]);
                    first++;
                    second = first;
                    result++;
                }
            } else{
                numMap.add(nums[first]);
                first++;
                second++;
                result++;
            }
        }

        return result;
    }
}