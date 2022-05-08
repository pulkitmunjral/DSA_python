#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from queue import PriorityQueue


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        q = PriorityQueue()
        for i in nums:
            q.put(i)
        for i in range(len(nums)-k):
            q.get()
        return q.get()
# @lc code=end

