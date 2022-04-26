#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.helper(res,nums,[])
        return res
    def helper(self,res,nums,path):
        res.append(path)
        for i in range(len(nums)):
            self.helper(res,nums[i+1:],path+[nums[i]])



        
# @lc code=end

