#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import re


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head==None or head.next==None):return None
        count = 1
        temp = head
        previous = None
        while temp.next:
            count+=1
            previous = temp
            temp = temp.next

        if n ==1:
            previous.next = None
            return head

        count-=n
        temp = head
        previous = None
        while count:
            previous = temp
            temp = temp.next
            count-=1

        if previous == None and count<=0:
            return head.next

        
        previous.next = temp.next
        return head
        


# @lc code=end

