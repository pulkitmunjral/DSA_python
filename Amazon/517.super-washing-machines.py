#
# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#

# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:

        l = len(machines)
        s = sum(machines)
        
        if s%l==0:
            target = s//l
            inout = 0
            ans = 0

            for i in machines:
                inout += i-target

                ans = max(ans,abs(inout),i-target)
            
            return ans

        else:
            return -1
   
# @lc code=end

