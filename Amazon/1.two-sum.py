#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        see = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in see.keys():
                return [see[sub],i]
            else:
                see[nums[i]]=i        
# @lc code=end

