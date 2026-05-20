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
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null){
            return new ArrayList<Integer>();
        }
        List<Integer> result = new ArrayList<>();
        if (root.left != null){
            List<Integer> leftTree = postorderTraversal(root.left);
            result.addAll(leftTree);
        }
        if (root.right != null){
            List<Integer> rightTree = postorderTraversal(root.right);
            result.addAll(rightTree);
        }
        result.add(root.val);
        return result;
    }
}