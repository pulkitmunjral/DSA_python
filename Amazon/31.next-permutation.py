#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        there is a pattern from left to right the number is in increasing order 
        and then there is a break point, we need to find that break point value (firstwhile loop do this)
        then we need to swap the break point with the next greater element to that break point from left to right 
        then just reverse the array from left to right till this break point.

        """
        def reverse_arr(arr, i):
            start = i
            end = len(arr)-1
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1

        l = len(nums)
        i = l-2
        while i>=0 and nums[i+1]<=nums[i]:
            i-=1
        
        if i>=0:
            j = l-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i], nums[j]=nums[j], nums[i]
        reverse_arr(nums, i+1)
# @lc code=end

