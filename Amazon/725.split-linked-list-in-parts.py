#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        new_head = head
        count = 0
        while head:
            head = head.next
            count+=1
        print(count)
        width, remainder = divmod(count, k)
        
        ans = [ListNode('')]*k
        
        cur = new_head
        
        for i in range(k):
            head = cur
            
            for j in range(width + (i<remainder)-1):
                if cur:
                    cur = cur.next

            if cur:
                cur.next, cur = None, cur.next
            ans[i]=head
        return ans

# @lc code=end

