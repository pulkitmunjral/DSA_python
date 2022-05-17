#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        col = set()
        row = set()
        x = len(matrix)
        y = len(matrix[0])

        for i in range(x):
            for j in range(y):
                if matrix[i][j]==0:
                    col.add(j)
                    row.add(i)

        for i in range(x):
            for j in range(y):
                if i in row or j in col:
                    matrix[i][j]=0
        


        
# @lc code=end

