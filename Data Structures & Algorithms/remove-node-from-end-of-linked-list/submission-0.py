# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        index_remove = count - n
        curr_index = 0
        prev = ListNode()
        dummy = prev
        curr = head
        prev.next = curr

        while curr:
            if curr_index == index_remove:
                prev.next = curr.next
                    
            curr_index += 1
            prev = curr
            curr = curr.next
        
        return dummy.next
            