#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#

# @lc code=start
from shutil import move


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        row = len(forest)
        col = len(forest[0])
                
        def bfs(x, y, i, j):
            x_moves = [0,0,1,-1]
            y_moves = [1,-1,0,0]

            q = [(x, y)]
            visited = set((x, y))
            move = 0
            while q:
                for _ in range(len(q)):
                    cur_x,cur_y = q.pop(0)
                    if (cur_x, cur_y) == (i, j):
                        return move
                        
                    for k in range(4):

                        x = cur_x + x_moves[k]
                        y = cur_y + y_moves[k]
                        if x>=0 and x<row and y>=0 and y<col and (x, y) not in visited and forest[x][y]:

                            q.append((x,y))
                            visited.add((x, y))
                move+=1
            return -1

        trees = [(i,j) for i in range(row) for j in range(col) if forest[i][j]>1] 
        trees = sorted(trees, key=lambda p:forest[p[0]][p[1]])
        total_step, x, y = 0, 0, 0
        for tx, ty in trees:
            step = bfs(x, y, tx, ty)
            if step==-1:
                return -1
            total_step += step
            x, y = tx, ty
        
        return total_step

# @lc code=end

