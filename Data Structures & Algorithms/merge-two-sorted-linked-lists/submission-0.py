# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        dummy = ListNode()
        head = dummy
        curr1 = list1
        curr2 = list2

        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    head.next = curr1
                    curr1 = curr1.next
                else:
                    head.next = curr2
                    curr2 = curr2.next
                head = head.next
            elif curr1:
                head.next = curr1
                break
            else:
                head.next = curr2
                break
        
        return dummy.next
