# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        h = head
        lenght = 0
        while h is not None:
            h = h.next
            lenght += 1
            
        def reorder(head, node):
            steps = lenght //2
            if node.next is not None:
                head, steps = reorder(head, node.next)
            
            if steps == 0:
                head.next = None
                return head, 0
            
            toReturn = head.next
            
            head.next = node
            node.next = toReturn

            return toReturn, steps - 1
        
        reorder(head, head)