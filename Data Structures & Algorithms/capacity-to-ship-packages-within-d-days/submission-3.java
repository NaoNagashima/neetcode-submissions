class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left = Arrays.stream(weights).max().getAsInt();
        int right = Arrays.stream(weights).sum();
        int result = right;

        while (left <= right){
            int maximumCapacity = left + (right - left) / 2;
            int capacity = 0;
            int ships = 1;
            for (int weight: weights){
                if (capacity + weight> maximumCapacity){
                    capacity = 0;
                    ships++;
                }
                capacity += weight;
            }

            if (ships <= days){
                result = Math.min(maximumCapacity, result);
                right = maximumCapacity - 1;
            } else{
                left = maximumCapacity + 1;
            }
        }
        return result;
    }
}