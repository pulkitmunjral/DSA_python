#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        ans = temp = ListNode(0)
        while list1 or list2:
            if list1 and list2:
                list2_value = list2.val
                list1_value = list1.val
                if list1_value > list2_value:
                    value = list2_value
                    list2 = list2.next
                else:
                    value = list1_value
                    list1 = list1.next
            elif list1:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next

            temp.next = ListNode(value)
            temp = temp.next
            
        return ans.next
                
# @lc code=end

