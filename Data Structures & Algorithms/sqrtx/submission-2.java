class Solution {
    public int mySqrt(int x) {
        int left = 1;
        int right = x;
        int result = 0;

        while (left <= right){
            int mid = left + (right - left) / 2;

            if ((long)mid * mid == x){
                return mid;
            } else if ((long)mid * mid > x){
                right = mid - 1;
            } else {
                left = mid + 1;
                result = mid;
            }
        }

        return result;

    }
}