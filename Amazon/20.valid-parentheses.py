#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        ans = []

        for i in s:
            if len(ans)>0 and  (i == ')' and '('==ans[-1]):
                ans.pop()
            elif len(ans)>0 and (i == ']' and '['==ans[-1]):
                ans.pop()
            elif len(ans)>0 and  (i == '}' and '{'==ans[-1]):
                ans.pop()
            else:
                ans.append(i)
        return True if len(ans)==0 else False
            
        
                    
# @lc code=end

