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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0 || inorder.length == 0){
            return null;
        }

        int root = preorder[0];
        int mid = -1;

        for (int i = 0; i < inorder.length; i++){
            if (root == inorder[i]){
                mid = i;
                break;
            }
        }

        int[] leftPreorder = Arrays.copyOfRange(preorder, 1, mid+1);
        int[] leftInorder = Arrays.copyOfRange(inorder, 0, mid);
        TreeNode leftNode = buildTree(leftPreorder, leftInorder);

        int[] rightPreorder = Arrays.copyOfRange(preorder, mid+1, preorder.length);
        int[] rightInorder = Arrays.copyOfRange(inorder, mid+1, inorder.length);
        TreeNode rightNode = buildTree(rightPreorder, rightInorder);

        TreeNode rootNode = new TreeNode(root);
        rootNode.left = leftNode;
        rootNode.right = rightNode;

        return rootNode;

    }
}
