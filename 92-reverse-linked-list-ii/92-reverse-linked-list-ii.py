# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lnode = head
        beforeswap = None
        for i in range(left-1):
            beforeswap = lnode
            lnode = lnode.next
        endswap = lnode
        _next=lnode.next
        for j in range(right-left):
            if _next is not None:
                prev = lnode
                lnode = _next
                _next = lnode.next
                # print(lnode, prev)
                lnode.next = prev
            # print(lnode.val, lnode.next.val)
        # print(beforeswap.val, lnode.val, endswap.val, next)
        if beforeswap is not None:
            beforeswap.next = lnode
        else:
            head=lnode
        endswap.next = _next
        # print(head)
        return head