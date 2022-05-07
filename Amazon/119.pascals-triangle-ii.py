#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start



class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        ans = [1,1]
        
        while rowIndex>1:
            temp = [1]
            for i in range(len(ans)-1):
                temp.append(ans[i]+ans[i+1])
            temp.append(1)
            ans = temp
            rowIndex-=1

        return ans

        
# @lc code=end

