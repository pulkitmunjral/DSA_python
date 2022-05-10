#
# @lc app=leetcode id=640 lang=python3
#
# [640] Solve the Equation
#

# @lc code=start
import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        lhs = 0
        rhs = 0
        l, r = equation.split("=")
        l = re.split("(?=\\+)|(?=-)",l)
        r = re.split("(?=\\+)|(?=-)",r)
        
        def getCof(temp,i):
            if temp>1 and i[temp-2]>='0' and i[temp-2]<='9':
                return int(i.replace('x',''))
            else:
                return int(i.replace('x','1'))

        for i in l:
            temp = len(i)
            if "x" in i:
                 lhs += getCof(temp, i)
            elif temp>0:
                rhs -= int(i)
        
        for i in r:
            temp = len(i)
            if "x" in i:
                lhs -= getCof(temp, i)
            elif temp>0:
                rhs += int(i)
                
        if lhs == 0:
            if rhs == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(int(rhs/lhs))
        
# @lc code=end

