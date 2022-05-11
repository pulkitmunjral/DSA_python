#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])

        x = row-1
        y = 0
        while x>=0 and y<col:
            cur = matrix[x][y]
            if target == cur:
                return True
            elif target< cur:
                x-=1
            else:
                y+=1
        
        return False

# @lc code=end

