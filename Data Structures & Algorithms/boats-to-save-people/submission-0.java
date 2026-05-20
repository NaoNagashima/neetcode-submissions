class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int start = 0;
        int end = people.length - 1;
        int result = 0;
        Arrays.sort(people);

        while (start <= end){
            int remaining = limit -  people[end--];
            if (start <= end && remaining >= people[start]){
                start++;
            }
            result++;
        }
        return result;
    }
}