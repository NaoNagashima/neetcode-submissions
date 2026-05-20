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
    public List<Integer> preorderTraversal(TreeNode root) {
        if (root == null){
            return new ArrayList<Integer>();
        }
        List<Integer> result = new ArrayList<>();
        result.add(root.val);
        if (root.left != null){
            List<Integer> leftTree = preorderTraversal(root.left);
            result.addAll(leftTree);
        }
        if (root.right != null){
            List<Integer> rightTree = preorderTraversal(root.right);
            result.addAll(rightTree);
        }
        return result;
    }
}