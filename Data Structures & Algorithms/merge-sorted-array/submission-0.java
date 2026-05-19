class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] num1Copy = Arrays.copyOf(nums1, m);
        int resIndex = 0;
        int i = 0;
        int j = 0;

        while (resIndex < m + n){
            if (j >= n || ( i < m && num1Copy[i] <= nums2[j])){
                nums1[resIndex] = num1Copy[i];
                resIndex++;
                i++;
            } else {
                nums1[resIndex] = nums2[j];
                resIndex++;
                j++;
            }
        }
    }
}