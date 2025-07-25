# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        carry_over = 0
        
        while l1 or l2 or carry_over:
            total = carry_over

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            digit = total % 10
            carry_over = total // 10

            dummy.next = ListNode(digit)
            dummy = dummy.next

        return result.next
