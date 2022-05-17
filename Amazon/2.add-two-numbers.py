#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0 
        temp = ans = ListNode(0)
        while l1 or l2:
            l1_current = 0
            l2_current = 0
            if l1:
                l1_current = l1.val
                l1 = l1.next
            if l2:
                l2_current = l2.val
                l2 = l2.next
            sum =  l1_current +  l2_current + carry
            value = sum%10
            carry = sum//10
            temp.next = ListNode(value)
            temp = temp.next
        if carry>0:
            temp.next = ListNode(carry)
        
        return ans.next


# @lc code=end

