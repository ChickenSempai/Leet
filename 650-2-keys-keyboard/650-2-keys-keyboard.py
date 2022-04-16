class Solution:

    def getnext(self, value, step, n):
        if value > n:
            return -1
        if value == n:
            return 0

        res = self.getnext(value*2, value, n)
        if res != -1:
            return res+2
        res = self.getnext(value+step, step, n)
        if res != -1:
            return res+1

        return -1


    def minSteps(self, n: int) -> int:
        step = 0
        value = 1
        return self.getnext(1, 0, n)