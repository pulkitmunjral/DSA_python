#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        
        l = len(nums)
        ans = [1]*l
        temp_r = 1
        temp_l = 1
        for i in range(l):
            ans[i]*=temp_r
            temp_r*=nums[i]
            ans[l-i-1]*=temp_l
            temp_l*=nums[l-i-1]

        # temp = 1
        # for i in range(len(nums)-1,-1,-1):
        #     ans[i]*=temp
        #     temp *= nums[i]
        
        return ans
# @lc code=end

