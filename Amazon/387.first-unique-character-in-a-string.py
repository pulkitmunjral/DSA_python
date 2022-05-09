#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        o = OrderedDict()

        for i,j in enumerate(s):
            if j in o:
                o[j][0]+=1
            else:
                o[j]=[1,i]
        
        for i,j in o.items():
            if j[0]==1:
                return j[1]
        return -1
# @lc code=end

