#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        temp = ""
        max = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in dic.keys():
                if len(temp)>max:
                    max=len(temp)
                temp = temp[dic[ch]+1:]
                temp+=ch
                new = {}
                for x in range(len(temp)):
                    new[temp[x]]=x
                dic = new
            else:
                dic[ch]=len(temp)
                temp+=ch
            if len(temp)>max:
                max=len(temp)
            

        return max

        
# @lc code=end

