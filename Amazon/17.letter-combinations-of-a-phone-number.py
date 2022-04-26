#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
import re


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        val = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        
        l = len(digits)
        if l==0:
            return []
        ans = val[digits[0]]
        k = 1
        while l>1:
            it = val[digits[k]]
            temp = []
            for i in ans:
                for j in it:
                    temp.append(i+j)
            ans = temp
            l-=1
            k+=1

        return ans

# @lc code=end

