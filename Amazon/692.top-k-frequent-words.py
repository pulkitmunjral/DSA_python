#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
import re


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dic = {}
        count = 0
        for i in words:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
                count+=1

        ans = [[] for _ in range(len(words))]

        for key,val in dic.items():
            ans[val].append(key)
        ans = ans[::-1]
        result = []
        i=0
        while k>len(result):
            ans[i].sort()
            result.extend(ans[i])
            i+=1
        
        return result[0:k]

        
# @lc code=end

