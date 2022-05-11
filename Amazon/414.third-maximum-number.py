#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
from queue import PriorityQueue


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        if len(nums)<3:
            return nums[-1]
        
        
        


        return nums[-3]
        
# @lc code=end

