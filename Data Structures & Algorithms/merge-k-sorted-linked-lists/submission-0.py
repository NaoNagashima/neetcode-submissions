# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists == [[]]:
            return None
        
        if len(lists) == 1:
            return lists[0]
        else:
            node1 = lists[0]
            node2 = lists[1]
            dummy = ListNode()
            result = dummy

            while node1 or node2:
                if node1 and node2:
                    if node1.val > node2.val:
                        result.next = node2
                        result = result.next
                        node2 = node2.next
                    else:
                        result.next = node1
                        result = result.next
                        node1 = node1.next
                elif node1:
                    result.next = node1
                    break
                else:
                    result.next = node2
                    break
            
            if len(lists) > 2:
                return self.mergeKLists([dummy.next]+lists[2:])
            return dummy.next