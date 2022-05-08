#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dic = {}
        ans = []
        for index,i in enumerate(numbers):
            sub = target - i
            if sub in dic:
                return [dic[sub],index+1]
            else:
                dic[i]=index+1
# @lc code=end

