#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans =set()

        def sub(candidates,li,i,target):
            
            if target==0:
                ans.add(tuple(sorted(li)))
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j]>target:
                    break
            
                li.append(candidates[j])
                sub(candidates,li,j+1,target-candidates[j])
                li.pop()
        candidates.sort()
        sub(candidates,[],0,target)
        return ans

# @lc code=end

