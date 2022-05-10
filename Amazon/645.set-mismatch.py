#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = [0]*len(nums)

        for i in nums:
            s[i-1]+=1

        return [1+s.index(2),1+s.index(0)]
        
# @lc code=end

