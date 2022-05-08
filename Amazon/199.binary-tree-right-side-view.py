#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def rightViewTree(root, level, li):

            global maxLevel
            if not root:
                return

            if level > maxLevel:
                li.append(root.val)
                maxLevel = level
            
            rightViewTree(root.right, level+1,li)
            rightViewTree(root.left, level+1,li)
       
        li=[]
        global maxLevel
        maxLevel = -1
        rightViewTree(root, 0, li)
        return li
        
# @lc code=end

