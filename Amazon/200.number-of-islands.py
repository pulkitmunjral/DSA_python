#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        x_move = [0, 1, 0, -1]
        y_move = [1, 0, -1 ,0]

        q =[]
        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    grid[row][col] = 0
                    count+=1
                    q.append((row, col))

                    while q:
                        current_x, current_y = q.pop(0)
                        for i in range(4):
                            x = current_x + x_move[i]
                            y = current_y + y_move[i]

                            if x>=0 and x<rows and y>=0 and y<cols and grid[x][y] == "1":
                                grid[x][y] = 0
                                q.append((x,y))
                                print(x, y)

        return count

                            
# @lc code=end

