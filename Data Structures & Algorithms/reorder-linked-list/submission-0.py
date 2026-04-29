# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val)
        
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # [0 1 2 3] [6 5 4]

        dummy = head
        curr = prev
        while curr:
            temp1 = dummy.next
            temp2 = curr.next
            dummy.next = curr
            curr.next = temp1
            dummy, curr = temp1, temp2


        


        
