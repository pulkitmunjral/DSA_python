#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        amount = len(lists)
        interval = 1

        while interval<amount:
            for i in range(0,amount-interval,interval*2):
                lists[i] = self.merge2(lists[i],lists[i+interval])
            interval*=2
        return lists[0] if amount>0 else None

    def merge2(self, l1, l2):
        head = pointer = ListNode(0)

        while l1 and l2:
            if l1.val<=l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next

            pointer = pointer.next
        if l1:
            pointer.next = l1
        else:
            pointer.next = l2
        return head.next

# @lc code=end

