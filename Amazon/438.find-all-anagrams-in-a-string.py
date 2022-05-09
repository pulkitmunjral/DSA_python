#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        temp = [0]*26
        temp2 = [0]*26

        for i in p:
            temp[ord(i)-ord('a')]+=1
        
        len_s = len(s)
        len_p = len(p)
        tt = s[:len_p]

        for i in tt:
            temp2[ord(i)-ord('a')]+=1
        ans = [0] if temp2 == temp else []

        for i in range(0,len_s-len_p):
            temp2[ord(s[i+len_p])-ord('a')]+=1
            temp2[ord(s[i])-ord('a')]-=1
            if temp2 == temp:
                ans.append(i+1)
        
        return ans



        
# @lc code=end

