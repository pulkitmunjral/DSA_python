#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return root

        if p.val<root.val and q.val<root.val:
            print("going left")
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        print("at last")
        return root
        
# @lc code=end

