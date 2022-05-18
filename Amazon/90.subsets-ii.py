#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def sub(nums,n,i=0,ar=[]):
            if n==i:
                ans.add(tuple(sorted(ar)))
                return 

            ar.append(nums[i])
            sub(nums,n,i+1,ar)

            ar.pop()
            sub(nums,n,i+1,ar)
        
        sub(nums,len(nums))
        return list(ans)
            
# @lc code=end

