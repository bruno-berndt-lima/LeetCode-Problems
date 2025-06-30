# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        ll_length = 1
        dummy = head

        while dummy.next:
            dummy = dummy.next
            ll_length += 1

        pos = k % ll_length
        if pos == 0:
            return head

        curr = head
        for i in range(ll_length - pos - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        dummy.next = head

        return new_head
