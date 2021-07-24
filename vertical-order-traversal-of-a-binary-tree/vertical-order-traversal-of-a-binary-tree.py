class HeapNode:
    def __init__(self, left=None, right=None):
        self.val = dict()
        self.left = left
        self.right = right

def addColLeft(root):
    root.left = HeapNode()
    root.left.right = root
    return root.left
    
def addColRight(root):
    root.right = HeapNode()
    root.right.left = root
    return root.right

def rec(head, root, deep):
    if root is None:
        return
    if head.val.get(deep) is None:
        head.val[deep] = []
    heap = head.val[deep]
    heapq.heappush(heap, root.val)

    if head.left is None and root.left is not None:
        rec(addColLeft(head), root.left, deep + 1)
    else:
        rec(head.left, root.left, deep + 1)
    if head.right is None and root.right is not None:
        rec(addColRight(head), root.right , deep + 1)
    else:
        rec(head.right, root.right, deep + 1) 
        
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        head = HeapNode()
        head.val[0] = []
        heapq.heappush(head.val[0], root.val)
        if root.left is not None:
            rec(addColLeft(head), root.left, 1)
        if head.right is None and root.right is not None:
            rec(addColRight(head), root.right, 1)
        else:
            rec(head.right, root.right, 1)
        leftest = head
        while leftest.left is not None:
            leftest = leftest.left
        res = []
        while leftest is not None:
            subres = []
            for key, heap in sorted(leftest.val.items()):
                while heap:
                    subres.append(heapq.heappop(heap))
            leftest = leftest.right
            res.append(subres)
        return res

    