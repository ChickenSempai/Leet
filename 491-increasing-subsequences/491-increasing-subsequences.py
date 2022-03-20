class Solution:
    res = []
    rep_barrier = set()
    def print_subs(self, nums, index, res):
        if index == len(nums):
            if len(res)>=2:
                string = str(res)
                if string not in self.rep_barrier:
                    self.rep_barrier.add(string)
                    self.res.append(res)
            return
        self.print_subs(nums, index+1, res.copy())
        if len(res)==0 or nums[index]>=res[-1]:
            res.append(nums[index])
            self.print_subs(nums, index+1, res.copy())

            
    def findSubsequences(self, nums):
        self.res = []
        self.rep_barrier = set()
        self.print_subs(nums, 0, [])
        return self.res