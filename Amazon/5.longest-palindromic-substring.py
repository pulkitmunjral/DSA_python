#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
from os import pread
import re


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
            
        i = 0 
        temp = s[0]
        max = ""
        for i in range(len(s)):
            j=len(s)-1
            while i<j:
                if s[i]==s[j]:
                    temp = s[i:j+1]
                    if temp == temp[::-1]:
                        break
                    else:
                        temp = s[0]
                j-=1

            if len(temp)>len(max):
                max = temp
        return max
                
        
# @lc code=end

