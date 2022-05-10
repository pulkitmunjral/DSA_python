#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from queue import PriorityQueue


class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}

        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        q = PriorityQueue()
        for key,val in dic.items():

            q.put((val,str( key)))
        
        ans=""
        while not q.empty():
            val,key = q.get()
            ans+= key*val
        
        print(ans)
        return ans[::-1]
        
        
# @lc code=end

