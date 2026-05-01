"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        map_copy = {}

        while curr:
            deepcopy = Node(curr.val)
            map_copy[curr] = deepcopy
            curr = curr.next
        
        curr = head

        while curr:
            print(curr.val)
            copy = map_copy[curr]
            if curr.random:
                copy.random = map_copy[curr.random]
            if curr.next:
                copy.next = map_copy[curr.next]
            curr = curr.next
        
        return map_copy[head]
            


            