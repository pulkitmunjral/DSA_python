#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = set()
        
        def sub(s,n,start=0,li=[]):
            if start>=n:
                ans.add(tuple(li))
                 
            
            for end in range(start,n):
                temp = s[start:end+1]
                if temp==temp[::-1]:
                    li.append(temp)
                    sub(s,n,end+1,li)
                    li.pop()
        
        sub(s,len(s))
        return ans
# @lc code=end

