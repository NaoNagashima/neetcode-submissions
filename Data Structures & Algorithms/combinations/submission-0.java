class Solution {

    public List<List<Integer>> result;

    public List<List<Integer>> combine(int n, int k) {
        result = new ArrayList<>();
        backtrack(1, n, k, new ArrayList<>());
        return result;
    }

    public void backtrack(int first, int n, int k, List<Integer>curr){
        if (curr.size() == k){
            result.add(new ArrayList<>(curr));
            return;
        }

        for (int i = first; i <= n; i++){
            curr.add(i);
            backtrack(i+1, n, k, curr);
            curr.remove(curr.size()-1);
        }
    }
}