#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        lenght = len(nums)

        sum_of_all = sum(nums)

        f0 = sum([i*e for i,e in enumerate(nums) ])

        max_sum = f0
        
        for i in range(lenght-1,0,-1):
            f0 += sum_of_all - nums[i]*lenght
            max_sum = max(f0,max_sum)

        return max_sum


# @lc code=end

