#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l = len(nums)
        # s = []
        # ans = [0]*l
        # for i in range(l-1,-1,-1):

        #     while s and nums[i]>=nums[s[-1]]:
        #         s.pop()

        #     if s:
        #         ans[i]=s[-1]
        #     else:
        #         ans[i]=l
        #     s.append(i)

        # ns = []
        # print(ans)
        # for i in range(l - k + 1):
        #     j = i

        #     while ans[j]<i+k:
        #         j = ans[j]
        #     ns.append(nums[j])
        # return ns\

        l = 0
        res = []
        q = []
        
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # when finish one window, left window moves to next, we need to pop off elements in q and start from 0
            if l > q[0]:
                q.pop(0)
                
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

        return res


# @lc code=end

