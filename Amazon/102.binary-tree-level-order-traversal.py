#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from re import A


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [(root,0)]

        ans = defaultdict(list)

        while q:
            now, level = q.pop(0)
            if now:
                ans[level].append(now.val)

                q.append((now.left,level+1))
                q.append((now.right,level+1))

        res = []
        for value in ans.values():
            res.append(value)
        return res
# @lc code=end

