#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
import queue


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)

        def convert(pos):
            row, col = divmod(pos - 1, n)

            if row%2 != 0:
                col = n - 1 - col
            row = abs(row - n + 1)
            return (row, col)


        dict = {}

        for i in range(1,n**2 + 1):
            row, col = convert(i)
            if board[row][col] > -1:
                dict[i] = board[row][col]
        
        target = n**2 
        start = 1
        moves = 0
        q = [(start,moves)]
        seen = {1}
        while q:
            pos, mov = q.pop(0)
            if pos in dict:
                pos = dict[pos]
            if pos == target:
                return mov
            for i in range(1,7):
                newpos = min(pos + i, target)
                if newpos not in seen:
                    seen.add(newpos)
                    q.append((newpos, mov + 1))
        return -1 



    
    
# @lc code=end

