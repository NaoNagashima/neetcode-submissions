/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    public HashMap<TreeNode, Integer> cache;

    public int rob(TreeNode root) {
        cache = new HashMap<>();
        cache.put(null, 0);
        return dfs(root);
    }

    public int dfs(TreeNode root){
        if (cache.containsKey(root)){
            return cache.get(root);
        }

        int result = root.val;
        if (root.left != null){
            result += dfs(root.left.left) + dfs(root.left.right);
        }
        if (root.right != null){
            result += dfs(root.right.left) + dfs(root.right.right);
        }

        result = Math.max(result, dfs(root.left) + dfs(root.right));
        cache.put(root, result);
        return result;
    }
}