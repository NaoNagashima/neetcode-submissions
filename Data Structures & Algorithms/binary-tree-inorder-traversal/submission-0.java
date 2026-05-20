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
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null){
            return new ArrayList<Integer>();
        }
        List<Integer> result = new ArrayList<>();
        if (root.left == null && root.right == null){
            result.add(root.val);
            return result;
        } 
        
        if (root.left != null){
            List<Integer> leftTree = inorderTraversal(root.left);
            result.addAll(leftTree);
        }

        result.add(root.val);

        if (root.right != null){
            List<Integer> rightTree = inorderTraversal(root.right);
            result.addAll(rightTree);
        }

        return result;

    }
}