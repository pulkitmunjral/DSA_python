#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkTree(root, min, max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False

            left = checkTree(root.left, min, root.val)

            if left:
                right = checkTree(root.right, root.val, max)
                return right
            return False

        return checkTree(root, -2**32, 2**32)
        
# @lc code=end

