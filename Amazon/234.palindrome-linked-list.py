#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        def secondHalf(head):
            slow = head
            fast = head

            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(head):
            previous = None
            current = head
            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous


        first_half = secondHalf(head)
        second_half = reverse(first_half.next)

        result = True

        while result and second_half is not None:

            if second_half.val != head.val:
                result = False
            second_half = second_half.next
            head = head.next
        return result


# @lc code=end

