class Solution:

    def depth(self, root, val):
        if root is None:
            return val
        
        root.val += self.depth(root.right, val)
        retval = self.depth(root.left, root.val)
        return retval

    def convertBST(self, root):
        self.depth(root, 0)
        return root