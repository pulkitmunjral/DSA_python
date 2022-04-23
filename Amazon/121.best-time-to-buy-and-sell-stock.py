#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi, ma =10**5,0
        for i in prices:
            mi = min(i,mi)
            ma = max(ma,i-mi)
        return ma
# @lc code=end

