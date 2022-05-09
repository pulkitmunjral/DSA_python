#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
   
        def call(root,p,q):
            if root is None:
                return False
            
            right = call(root.right, p, q)
            left = call(root.left, p, q)
            mid = root == p or root ==q
            if mid + left + right>=2:

                self.ans = root
            
            return mid or left or right

        

        call(root,p,q)
        return self.ans
# @lc code=end

