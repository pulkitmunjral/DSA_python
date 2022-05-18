#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans =set()

        def sub(candidates,n,li,i,target):
            if i==n:
                if target==0:
                    ans.add(tuple(sorted(li)))
                return
            if candidates[i]<=target:
                li.append(candidates[i])
                sub(candidates, n,li,i,target-candidates[i])
                li.pop()
            sub(candidates, n,li,i+1,target)

        sub(candidates,len(candidates),[],0,target)
        return ans
# @lc code=end

