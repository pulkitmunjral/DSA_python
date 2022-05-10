#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # if root1 is None:
        #     return root2
        # if root2 is None:
        #     return root1
        
        # root1.val +=root2.val

        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)

        # return root1
        
        if root1 is None:
            return root2
        s = [(root1,root2)]

        while s:
            t1, t2 = s.pop()

            if t1 is None or t2 is None:
                continue

            t1.val +=t2.val
            
            if t1.left is None:
                t1.left = t2.left
            else:
                s.append((t1.left,t2.left))
            
            if t1.right is None:
                t1.right = t2.right
            else:
                s.append((t1.right,t2.right))
        
        return root1
            
# @lc code=end

