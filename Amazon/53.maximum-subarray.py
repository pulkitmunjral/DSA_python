#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maxSoFar = nums[0]
        l = len(nums)

        for i in range(1,l):
            current += nums[i]
            if current<nums[i]:
                current = nums[i]

            if maxSoFar<current:
                maxSoFar = current
        
        return maxSoFar
        
# @lc code=end

