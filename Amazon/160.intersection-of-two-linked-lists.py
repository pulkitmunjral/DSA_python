#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        ptrA = headA
        ptrB = headB

        lenA = 1
        lenB = 1
        while ptrA:
            ptrA = ptrA.next
            lenA+=1
        while ptrB:
            ptrB = ptrB.next
            lenB+=1

        if ptrB is not ptrA:
            return None
        else:
            if lenA < lenB:
                longest = headB
                shortest = headA
                skip = lenB - lenA
            else:
                longest = headA
                shortest = headB
                skip = lenA - lenB
            for i in range(skip):
                longest = longest.next
            
            while longest is not shortest:
                longest = longest.next
                shortest = shortest.next
            return longest


# @lc code=end

