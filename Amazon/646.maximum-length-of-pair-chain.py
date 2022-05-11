#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start



import operator


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        curr = -10**9
        ans = 0
        
        # by using sorted with key this will sort elements on the basis of 1st value instead of 0th 
        for i,j in sorted(pairs, key = operator.itemgetter(1)):
            if curr<i:
                curr=j
                ans+=1

        return ans  

        
# @lc code=end

