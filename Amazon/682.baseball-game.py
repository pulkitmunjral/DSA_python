#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []

        for i in ops:
            if i == "C":
                s.pop()
            elif i == "D":
                s.append(s[-1]*2)
            elif i == "+":
                s.append(s[-1]+s[-2])
            else:
                s.append(int(i))
        
        ans = 0
        for j in s:
            ans += j
        
        return ans
        
        
# @lc code=end

