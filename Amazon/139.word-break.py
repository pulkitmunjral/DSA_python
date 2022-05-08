#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start

class Solution:
    def wordBreak(self, s, wordDict):
        
        q = [0]
        visited = set()
        l = len(s)
        while q:
            start = q.pop(0)
            if start in visited:
                continue
            for end in range(start + 1,l + 1):
                if s[start:end] in wordDict:
                    if end == l:
                        return True
                    q.append(end)
            visited.add(start)
        return False

# @lc code=end

