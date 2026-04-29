# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        leading_zero = 0
        dummy = ListNode()
        result = dummy

        while l1 or l2:
            if l1 and l2:
                added_val = l1.val + l2.val + leading_zero
                if leading_zero != 0:
                    leading_zero -= 1
                val = added_val%10
                if added_val > 9:
                    leading_zero += 1
                result.next = ListNode(val)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                added_val = l1.val + leading_zero
                if leading_zero != 0:
                    leading_zero -= 1
                val = added_val % 10
                if added_val > 9:
                    leading_zero += 1
                result.next = ListNode(val)
                l1 = l1.next
            else:
                added_val = l2.val + leading_zero
                if leading_zero != 0:
                    leading_zero -= 1
                val = added_val % 10
                if added_val > 9:
                    leading_zero += 1
                result.next = ListNode(val)
                l2 = l2.next
            result = result.next
        
        if leading_zero != 0:
            result.next = ListNode(1)

        return dummy.next