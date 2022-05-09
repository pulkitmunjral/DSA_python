#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def d():
            return 0
        temp = defaultdict(d)
        if len(s)!=len(t):
            return False
        for i in s:

            temp[i]+=1

        
        for j in t:
            if j in temp and temp[j]>0:
                temp[j]-=1
            else:
                return False
        return True
# @lc code=end

