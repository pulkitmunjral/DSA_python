#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        k = 0
        while k<=j:

            if nums[k]==0:
                nums[k], nums[i]=nums[i], nums[k]
                i+=1
                k+=1
            elif nums[k]==2:
                nums[k], nums[j]=nums[j], nums[k]
                j-=1
            else:
                k+=1
        
# @lc code=end

