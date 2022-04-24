#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        low = 0
        high = len(nums)-1
        while low<=high:
            
            mid = (low+high)//2
            mid_value = nums[mid]
            if mid_value==target:
                return mid

            if mid_value > target:
                high = mid -1
            else:
                low = mid +1

        return low

        
# @lc code=end

