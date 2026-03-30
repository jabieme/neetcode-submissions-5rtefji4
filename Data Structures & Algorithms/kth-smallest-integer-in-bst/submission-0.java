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
    private List<Integer> kthSmallestList = new ArrayList<>();
    public void helper(TreeNode root){
        if(root == null){
            return;
        }
        helper(root.left);
        kthSmallestList.add(root.val);
        helper(root.right);
    }
    public int kthSmallest(TreeNode root, int k) {
        helper(root);
        return kthSmallestList.get(k-1);
    }
}
