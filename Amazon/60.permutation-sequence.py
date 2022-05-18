#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # ans = []
        # def permutations(remaining,candidate=''):
        #     if len(remaining) == 0:
        #         ans.append(candidate)
        #         if len(ans)==k:
        #             return
        #     for i in range(len(remaining)):
        
        #         newCandidate = candidate + remaining[i]
        #         newRemaining = remaining[0:i] + remaining[i+1:]
        
        #         permutations(newRemaining, newCandidate)
        
        # permutations('123456789'[:n])
        # return ans[k-1]
        ans = [""]
        def prem(n,k,li,fact):
            if n==1:
                ans[0]+=li[0]
                return 
            
            fact//=n
            ans[0]+=li.pop(k//fact)
            prem(n-1,k%fact,li,fact)

        fact = 1
        li = []
        for i in range(1,n+1):
            fact*=i
            li.append(str(i))
        prem(n,k-1,li,fact)
        
        return ans[0]

# @lc code=end

