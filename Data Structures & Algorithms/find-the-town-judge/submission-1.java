class Solution {

    public HashMap<Integer, Integer> trustMap;// [0] person id [1] # of trustees

    public int findJudge(int n, int[][] trust) {
        trustMap = new HashMap<>();
        for (int[] t: trust){
            if (!trustMap.containsKey(t[0])){
                trustMap.put(t[0], -1);
            } else {
                trustMap.put(t[0], -1);
            }

            if (!trustMap.containsKey(t[1])){
                trustMap.put(t[1], 1);
            } else{
                if (trustMap.get(t[1]) != -1){
                    trustMap.put(t[1], trustMap.get(t[1])+1);
                }   
            }
        }
        for (Integer person: trustMap.keySet()){
            if (trustMap.get(person) == n - 1){
                return person;
            }
        }
        return -1;
    }
}