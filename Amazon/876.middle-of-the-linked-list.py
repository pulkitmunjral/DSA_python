#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from os import pread


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count+=1
            temp = temp.next

        count//=2
        while count:
            count-=1
            head = head.next
        return head
# @lc code=end

