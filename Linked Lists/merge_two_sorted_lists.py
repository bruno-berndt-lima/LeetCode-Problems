# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = dummy_head = ListNode()
    
        while list1 and list2:
            if list1.val < list2.val:
                curr_node.next = list1
                list1, curr_node = list1.next, list1
            else:
                curr_node.next = list2
                list2, curr_node = list2.next, list2

        if list1 or list2:
            curr_node.next = list1 if list1 else list2

        return dummy_head.next
